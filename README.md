# Robotics Journey
Learning the full robotics stack: embedded → OS → ROS 2 → perception → control → sim/ML.

## Plan
- Weeks 1–4: Foundations (Linux, C++, linear algebra, physics sim from scratch)
- Weeks 5–9: Embedded + RTOS + OS concurrency (ESP32 motor controller)
- Weeks 10–14: ROS 2 + Gazebo (SLAM + Nav2 robot)
- Weeks 15–19: Perception + state estimation (EKF, AprilTags)
- Weeks 20–24: Control + RL (LQR, MuJoCo/Isaac Lab)
- Weeks 25–28: Capstone real robot

## Log
- **Nov 13, 2026:** Built 1D bouncing ball sim from scratch (01-BallSim). Learned:
  Euler integration, integer step counter to avoid float drift, floor collision,
  restitution. Bounce heights decay by e² (0.64) — matches physics.
