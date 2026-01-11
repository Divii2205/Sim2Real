import torch
import genesis as gs
from go2_env import Go2Env
from agent import Agent
import time
import pickle
import os

def main():
    gs.init(backend=gs.cpu)

    # Load configs
    with open(os.path.join("logs/go2-walking", "cfgs.pkl"), "rb") as f:
        env_cfg, obs_cfg, reward_cfg, command_cfg, train_cfg = pickle.load(f)

    reward_cfg["reward_scales"] = {}

    env = Go2Env(
        num_envs=1,
        env_cfg=env_cfg,
        obs_cfg=obs_cfg,
        reward_cfg=reward_cfg,
        command_cfg=command_cfg,
        show_viewer=True,
    )

    agent = Agent()

    def reset(self):
        self._reset_idx()
        self._update_observation()
        return self.obs_buf, None

    obs, _ = env.reset()

    with torch.no_grad():
        while True:
            actions = agent.apply(obs)
            obs, rewards, dones, infos = env.step(actions)
            time.sleep(1 / 60)

if __name__ == "__main__":
    main()
