import argparse
import os
import pickle
import time
import torch
import numpy as np
import genesis as gs
from go2_env import Go2Env
from rsl_rl.runners import OnPolicyRunner

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--exp_name", type=str, default="go2-walking")
    parser.add_argument("--ckpt", type=int, default=300) 
    parser.add_argument("--vel", type=float, default=2.5) # Start at a known training speed
    args = parser.parse_args()

    # Use CPU to match your original "working" setup
    gs.init(backend=gs.cpu)

    log_dir = f"checkpoints/"
    cfgs_path = os.path.join(log_dir, "cfgs.pkl")
    env_cfg, obs_cfg, reward_cfg, command_cfg, train_cfg = pickle.load(open(cfgs_path, "rb"))

    # --- MATCH TRAINING EXACTLY ---
    env_cfg["kp"] = 45.0             # Revert to your training gain
    env_cfg["kd"] = 1.0              # Revert to your training damping
    env_cfg["resampling_time_s"] = 1e6 
    reward_cfg["reward_scales"] = {} 

    env = Go2Env(
        num_envs=1,
        env_cfg=env_cfg,
        obs_cfg=obs_cfg,
        reward_cfg=reward_cfg,
        command_cfg=command_cfg,
        show_viewer=True,
    )

    runner = OnPolicyRunner(env, train_cfg, log_dir, device=gs.device)
    resume_path = os.path.join(log_dir, f"model_{args.ckpt}.pt")
    runner.load(resume_path)
    policy = runner.get_inference_policy(device=gs.device)

    obs, _ = env.reset()
    start_time = time.time()
    start_pos_x = None
    
    print(f"\n--- Testing at {args.vel} m/s (Matched Gains) ---")

    with torch.no_grad():
        while True:
            # LOCK THE COMMAND
            env.commands[:, 0] = args.vel
            env.commands[:, 1] = 0.0
            env.commands[:, 2] = 0.0

            actions = policy(obs)
            obs, rews, dones, infos = env.step(actions)

            # POSITION TRACKING
            current_x = env.base_pos[0, 0].item()
            if start_pos_x is None: start_pos_x = current_x
            
            displacement = current_x - start_pos_x
            elapsed = time.time() - start_time

            if int(elapsed * 10) % 10 == 0:
                print(f"Time: {elapsed:.1f}s | Dist: {displacement:.2f}m", end='\r')

            if dones.any() or elapsed >= 30:
                print(f"\nFinal Displacement: {displacement:.2f} meters")
                break

if __name__ == "__main__":
    main()