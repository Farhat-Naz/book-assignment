# Implementation Plan: Physical AI & Humanoid Robotics Course

**Branch**: `1-robotics-course-spec` | **Date**: 2025-12-05 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/1-robotics-course-spec/spec.md`

## Summary

This implementation plan details the complete architecture for developing a comprehensive, professional-level course on Physical AI & Humanoid Robotics. The course will be delivered as a Docusaurus-based static website with 8 modules, 36 chapters, 180 hours of content, including theoretical foundations, hands-on labs, and capstone projects. The course targets university students and professional engineers, providing complete, runnable code examples with scaffolding, hierarchical navigation, automated assessments, and multi-format visualizations.

## User Request Context

The user has explicitly requested a detailed, structured plan (not JSON) covering:

1. Finalized module list
2. Chapters inside each module
3. Sub-sections for each chapter
4. Practical labs and projects
5. Tools, libraries, and robotics hardware
6. Learning progression roadmap
7. Approximate page count for each module
8. Docusaurus folder structure plan
9. A milestone timeline
10. Cross-module knowledge dependencies

This plan will serve as the complete architecture before chapter writing begins.

## Technical Context

**Content Management System**: Docusaurus 2.x (Static Site Generator)
**Content Format**: Markdown with MDX components for interactive elements
**Primary Languages**: Python 3.10+, C++17/20 (for code examples)
**Robotics Frameworks**: ROS2 Humble LTS
**Simulation Environments**: PyBullet, Webots, MuJoCo, Gazebo
**AI/ML Frameworks**: PyTorch, TensorFlow, Stable-Baselines3, OpenAI Gym
**Computer Vision**: OpenCV, MediaPipe, YOLO, Open3D
**Development Tools**: Docker, Git, VS Code/PyCharm, RViz, Plotly/Matplotlib
**Testing**: Manual code verification, automated quiz plugins (JavaScript-based)
**Deployment Platform**: GitHub Pages with GitHub Actions CI/CD
**Version Control**: Git with feature-based branching
**Performance Goals**:
- Page load time <2 seconds for 95% of pages
- Search results in <2 seconds (FR-013, SC-012)
- 99% uptime on GitHub Pages (SC-011)
**Constraints**:
- Static site only (no backend/database)
- Content must be in Markdown/MDX format
- 100,000-150,000 total words across 36 chapters
- All code examples must run on minimum hardware (quad-core CPU, 8GB RAM)
**Scale/Scope**:
- 8 modules, 36 chapters, ~180 learning hours
- Estimated 3,000-4,200 words per chapter average
- 150-200 code examples total
- 25+ glossary terms
- 3 capstone projects

## Constitution Check

**Note**: This project is an educational course creation project, not traditional software development. Constitution principles are adapted for content creation:

✅ **Content-First Principle**: Each module is self-contained with clear learning objectives; modules build incrementally on prior knowledge

✅ **User-Centric Design**: All content focuses on learner needs (WHAT to learn, WHY it matters) before technical implementation (HOW)

✅ **Quality Assurance**: All code examples will be tested before publication; automated quizzes provide immediate feedback; manual review for complex assessments

✅ **Observability/Feedback**: Progress tracking (FR-014), search functionality (FR-013), responsive design (FR-012) ensure learner can navigate and monitor progress

✅ **Simplicity**: Hierarchical navigation (clarification Q2); complete code scaffolding (clarification Q1) avoids overwhelming learners while maintaining rigor

**No Constitution Violations**: This project follows principles adapted for educational content delivery

## Project Structure

### Documentation (this feature)

```
specs/1-robotics-course-spec/
├── spec.md                    # Feature specification (COMPLETED)
├── plan.md                    # This file - implementation plan
├── research.md                # Phase 0: Technology research and decisions
├── content-structure.md       # Detailed content hierarchy and page counts
├── docusaurus-config.md       # Docusaurus configuration decisions
├── milestone-timeline.md      # Development timeline and milestones
├── knowledge-dependencies.md  # Cross-module knowledge prerequisites
├── quickstart.md              # Quick start guide for contributors
├── checklists/
│   └── requirements.md        # Specification quality checklist (COMPLETED)
└── tasks.md                   # Phase 2 output (/sp.tasks command - NOT YET CREATED)
```

### Course Content Structure (Docusaurus Website)

```
docs/                          # All course content (Markdown/MDX)
├── index.md                   # Course homepage and overview
├── prerequisites/             # Prerequisites and self-assessment
│   ├── self-assessment.md
│   ├── python-refresher.md
│   ├── cpp-basics.md
│   ├── math-foundations.md
│   └── linux-setup.md
├── module-01-foundations/     # Module 1: Foundations of Physical AI
│   ├── index.md              # Module overview
│   ├── ch01-intro-physical-ai.md
│   ├── ch02-math-foundations.md
│   ├── ch03-robot-anatomy.md
│   └── ch04-ros2-architecture.md
├── module-02-kinematics/      # Module 2: Robot Kinematics and Motion Planning
│   ├── index.md
│   ├── ch05-forward-kinematics.md
│   ├── ch06-inverse-kinematics.md
│   ├── ch07-trajectory-planning.md
│   ├── ch08-motion-planning.md
│   └── ch09-whole-body-control.md
├── module-03-dynamics-control/  # Module 3: Dynamics and Control
│   ├── index.md
│   ├── ch10-rigid-body-dynamics.md
│   ├── ch11-control-theory.md
│   ├── ch12-advanced-control.md
│   ├── ch13-force-control.md
│   └── ch14-real-time-control.md
├── module-04-perception/      # Module 4: Perception and Sensor Processing
│   ├── index.md
│   ├── ch15-computer-vision.md
│   ├── ch16-object-detection.md
│   ├── ch17-slam.md
│   ├── ch18-sensor-fusion.md
│   └── ch19-point-clouds.md
├── module-05-locomotion/      # Module 5: Bipedal Locomotion
│   ├── index.md
│   ├── ch20-bipedal-fundamentals.md
│   ├── ch21-walking-controllers.md
│   ├── ch22-balance-control.md
│   ├── ch23-terrain-locomotion.md
│   └── ch24-running-jumping.md
├── module-06-ai-learning/     # Module 6: AI and Machine Learning
│   ├── index.md
│   ├── ch25-ml-fundamentals.md
│   ├── ch26-reinforcement-learning.md
│   ├── ch27-deep-rl.md
│   ├── ch28-imitation-learning.md
│   └── ch29-model-based-rl.md
├── module-07-hri/             # Module 7: Human-Robot Interaction
│   ├── index.md
│   ├── ch30-hri-fundamentals.md
│   ├── ch31-speech-nlp.md
│   ├── ch32-gesture-recognition.md
│   └── ch33-collaborative-tasks.md
├── module-08-integration/     # Module 8: Integration and Capstone
│   ├── index.md
│   ├── ch34-system-architecture.md
│   ├── ch35-testing-validation.md
│   ├── ch36-ethics-future.md
│   ├── capstone-project-1.md  # Autonomous Service Robot
│   ├── capstone-project-2.md  # Learning-Based Bipedal Walker
│   └── capstone-project-3.md  # Collaborative Assembly Robot
├── labs/                      # Hands-on lab guides
│   ├── lab-01-environment-setup/
│   ├── lab-02-transformation-math/
│   ├── lab-03-urdf-models/
│   ...
│   └── lab-36-ethics-case-studies/
├── code-examples/             # Complete, runnable code with scaffolding
│   ├── module-01/
│   │   ├── ch01-ros2-pub-sub/
│   │   ├── ch02-rotation-matrices/
│   │   ├── ch03-urdf-loading/
│   │   └── ch04-multi-node-system/
│   ├── module-02/
│   ...
│   └── module-08/
├── resources/                 # Supplementary resources
│   ├── datasets.md           # Dataset links and instructions
│   ├── tools-setup.md        # Tool installation guides
│   ├── hardware-guide.md     # Optional hardware recommendations
│   ├── troubleshooting.md    # Common issues and solutions
│   ├── research-papers.md    # Curated research paper list
│   └── external-resources.md # Books, courses, documentation links
├── assessments/               # Automated quizzes and rubrics
│   ├── quizzes/
│   │   ├── module-01-quiz.md
│   │   ├── module-02-quiz.md
│   │   ...
│   │   └── module-08-quiz.md
│   └── rubrics/
│       ├── lab-report-rubric.md
│       └── capstone-rubric.md
├── glossary.md                # Comprehensive technical glossary
├── faq.md                     # Frequently asked questions
└── about.md                   # About the course and authors

static/                        # Static assets
├── img/                       # Images, diagrams, illustrations
│   ├── robots/               # Robot photos and renders
│   ├── diagrams/             # Technical diagrams (PNG/SVG)
│   ├── screenshots/          # Software screenshots
│   └── visualizations/       # Data visualizations
├── models/                    # URDF models, meshes, configurations
│   ├── humanoid-simple/
│   ├── humanoid-atlas/
│   └── environments/
└── downloads/                 # Downloadable resources
    ├── code-archives/        # Zipped code examples per module
    ├── datasets/             # Mirrored datasets (if small enough)
    └── slides/               # Optional presentation slides

src/                           # Custom Docusaurus components
├── components/                # React/MDX components
│   ├── CodePlayground.js     # Interactive code editor (optional)
│   ├── Quiz.js               # Automated quiz component
│   ├── ProgressTracker.js    # Progress tracking component
│   └── DiagramRenderer.js    # Mermaid diagram renderer
├── css/                       # Custom styling
│   └── custom.css
└── pages/                     # Custom pages (non-docs)
    └── index.js              # Landing page

docusaurus.config.js           # Docusaurus configuration
sidebars.js                    # Hierarchical sidebar configuration
package.json                   # Node.js dependencies
```

**Structure Decision**: We are using Docusaurus's standard documentation structure with hierarchical modules as top-level categories and chapters as individual pages within each module. This aligns with clarification Q2 (hierarchical sidebar with auto-generated navigation) and supports the 8-module, 36-chapter architecture specified in the feature spec.

---

## 1. Finalized Module List

Based on the specification (courseStructure.modules), the course consists of **8 modules** with a total of **36 chapters**:

### Module 1: Foundations of Physical AI and Robotics
**Estimated Hours**: 18
**Chapters**: 4
**Focus**: Core concepts, mathematical foundations, robot anatomy, ROS2 basics

### Module 2: Robot Kinematics and Motion Planning
**Estimated Hours**: 24
**Chapters**: 5
**Focus**: Forward/inverse kinematics, trajectory planning, motion planning algorithms, whole-body control

### Module 3: Robot Dynamics and Control Systems
**Estimated Hours**: 22
**Chapters**: 5
**Focus**: Rigid body dynamics, control theory (PID, advanced control), force control, real-time systems

### Module 4: Perception and Sensor Processing
**Estimated Hours**: 26
**Chapters**: 5
**Focus**: Computer vision, object detection, SLAM, sensor fusion, point cloud processing

### Module 5: Bipedal Locomotion and Balance
**Estimated Hours**: 24
**Chapters**: 5
**Focus**: Walking fundamentals, gait generation, balance control, terrain navigation, dynamic locomotion

### Module 6: AI and Machine Learning for Robotics
**Estimated Hours**: 28
**Chapters**: 5
**Focus**: ML foundations, reinforcement learning, deep RL, imitation learning, model-based RL

### Module 7: Human-Robot Interaction and Collaboration
**Estimated Hours**: 20
**Chapters**: 4
**Focus**: HRI principles, speech/NLP, gesture recognition, collaborative task execution

### Module 8: System Integration and Capstone Projects
**Estimated Hours**: 38
**Chapters**: 3 + 3 Capstone Projects
**Focus**: Full-stack architecture, testing/validation, ethics, integration projects

---

## 2. Chapters Inside Each Module

*(Detailed chapter breakdown with sub-sections follows in section 3)*

### Module 1: Foundations (4 chapters)
1. Introduction to Physical AI and Embodied Intelligence
2. Mathematical Foundations for Robotics
3. Humanoid Robot Anatomy and Components
4. ROS2 Architecture and Communication Patterns

### Module 2: Kinematics (5 chapters)
5. Forward Kinematics and Denavit-Hartenberg Convention
6. Inverse Kinematics and Numerical Solutions
7. Trajectory Planning and Interpolation
8. Path and Motion Planning Algorithms
9. Whole-Body Motion Control

### Module 3: Dynamics and Control (5 chapters)
10. Rigid Body Dynamics and Equations of Motion
11. Fundamentals of Control Theory
12. Advanced Control Methods
13. Force Control and Physical Interaction
14. Real-Time Control Systems

### Module 4: Perception (5 chapters)
15. Computer Vision Fundamentals
16. Object Detection and Recognition
17. Simultaneous Localization and Mapping (SLAM)
18. Multi-Sensor Fusion and State Estimation
19. 3D Point Cloud Processing

### Module 5: Locomotion (5 chapters)
20. Fundamentals of Bipedal Locomotion
21. Walking Pattern Generation
22. Balance and Push Recovery
23. Locomotion on Uneven Terrain
24. Advanced Locomotion: Running and Jumping

### Module 6: AI and Learning (5 chapters)
25. Machine Learning Foundations for Robotics
26. Reinforcement Learning Fundamentals
27. Deep Reinforcement Learning
28. Imitation Learning and Learning from Demonstration
29. Model-Based RL and World Models

### Module 7: HRI (4 chapters)
30. Foundations of Human-Robot Interaction
31. Speech Recognition and Natural Language Processing
32. Gesture and Activity Recognition
33. Collaborative Task Execution

### Module 8: Integration (3 chapters + 3 projects)
34. Full-Stack Robotics System Architecture
35. Testing, Validation, and Safety
36. Ethics, Safety, and Future of Humanoid Robotics
- Capstone Project 1: Autonomous Service Robot
- Capstone Project 2: Learning-Based Bipedal Walker
- Capstone Project 3: Collaborative Assembly Robot

---

## 3. Sub-Sections for Each Chapter

### Module 1: Foundations of Physical AI and Robotics

#### Chapter 1: Introduction to Physical AI and Embodied Intelligence
**Estimated Pages**: 12-15

**Sub-Sections**:
1. What is Physical AI vs Traditional AI
   - Embodied vs disembodied intelligence
   - Sensor-motor loops and real-time constraints
   - Examples from nature and robotics
2. Embodied Cognition and Sensor-Motor Integration
   - Theoretical foundations
   - Perception-action coupling
   - Brooks' subsumption architecture
3. History and Evolution of Humanoid Robotics
   - Early humanoid projects (WABOT, ASIMO)
   - Modern platforms (Atlas, Optimus, Digit, Nao)
   - Timeline of key milestones
4. Key Challenges in Physical AI Systems
   - Real-world uncertainty
   - Hardware limitations
   - Safety and reliability
   - Sim-to-real transfer
5. Overview of Modern Humanoid Platforms
   - Commercial robots (Boston Dynamics Atlas, Tesla Optimus)
   - Research platforms (TALOS, iCub, Valkyrie)
   - Comparison of capabilities and specifications

**Practical Session**: Environment Setup and First ROS2 Node (3 hours)
- Install Ubuntu/Docker development environment
- Install ROS2 Humble
- Create and run first ROS2 publisher/subscriber
- Explore ROS2 command-line tools

**Learning Objectives**:
- Define physical AI and distinguish from traditional AI
- Identify key components of humanoid robotic systems
- Explain the role of embodiment in intelligent behavior

---

#### Chapter 2: Mathematical Foundations for Robotics
**Estimated Pages**: 18-22

**Sub-Sections**:
1. Vectors, Matrices, and Coordinate Systems
   - Vector operations and notation
   - Matrix algebra essentials
   - Coordinate frames and transformations
2. Rotation Representations
   - Euler angles and gimbal lock
   - Rotation matrices (SO(3))
   - Quaternions and advantages
   - Axis-angle representation
3. Homogeneous Transformations and Spatial Relationships
   - 4x4 transformation matrices (SE(3))
   - Composing transformations
   - Inverse transformations
4. Velocity and Acceleration in 3D Space
   - Linear and angular velocity
   - Time derivatives of rotations
   - Twist coordinates
5. Numerical Methods for Robotics
   - Numerical differentiation and integration
   - Root finding (Newton-Raphson)
   - Matrix decompositions (SVD, QR)

**Practical Session**: Transformation Mathematics in Python (4 hours)
- Implement rotation matrix operations
- Work with transformation libraries (NumPy, transforms3d)
- Visualize coordinate frames with Matplotlib
- Solve forward kinematics for simple robot arm

**Learning Objectives**:
- Apply transformation mathematics to robot pose problems
- Convert between different rotation representations
- Compute spatial relationships between coordinate frames

**Mathematical Depth**: Key derivations step-by-step (per clarification Q3)
- Derivation of rotation matrix from Euler angles
- Proof of quaternion normalization
- Transformation composition derivation

---

#### Chapter 3: Humanoid Robot Anatomy and Components
**Estimated Pages**: 14-16

**Sub-Sections**:
1. Mechanical Structure and Degrees of Freedom
   - Kinematic chains
   - DOF calculation and constraints
   - Typical humanoid DOF distribution
2. Actuators: Motors, Servos, and Hydraulics
   - DC motors and gearboxes
   - Servo motors and control
   - Hydraulic actuators
   - Comparison and applications
3. Sensors: IMU, Encoders, Force/Torque, Vision
   - Inertial Measurement Units (IMU)
   - Joint encoders (absolute vs incremental)
   - Force/torque sensors
   - Cameras and depth sensors
4. Power Systems and Energy Management
   - Battery technologies
   - Power distribution
   - Energy efficiency considerations
5. Computing Architectures for Real-Time Control
   - Embedded controllers
   - CPU vs GPU vs FPGA
   - Real-time operating systems

**Practical Session**: Exploring Simulated Humanoid Models (3 hours)
- Load humanoid URDF models in RViz
- Inspect joint configurations and limits
- Visualize sensor placements
- Test basic joint control commands

**Learning Objectives**:
- Identify major components of humanoid robot hardware
- Understand sensor-actuator integration
- Analyze robot specifications for application requirements

---

#### Chapter 4: ROS2 Architecture and Communication Patterns
**Estimated Pages**: 16-20

**Sub-Sections**:
1. ROS2 Computational Graph
   - Nodes, topics, services, actions
   - Graph visualization and debugging
   - Naming and namespaces
2. DDS Middleware and Quality of Service
   - Data Distribution Service (DDS)
   - QoS profiles (reliability, durability, history)
   - Choosing appropriate QoS settings
3. Launch Files and Parameter Management
   - Launch file syntax and structure
   - Parameter servers
   - Dynamic reconfiguration
4. TF2 Coordinate Frame Management
   - TF2 tree structure
   - Broadcasting transforms
   - Looking up transforms
   - Time synchronization
5. ROS2 Development Tools and Debugging
   - rqt plugins
   - ros2bag for data recording
   - Debugging strategies
   - Performance profiling

**Practical Session**: Building Multi-Node ROS2 Systems (4 hours)
- Create package with multiple nodes
- Implement publisher-subscriber communication
- Create service server and client
- Write launch files for complex systems
- Debug using rqt and command-line tools

**Learning Objectives**:
- Design distributed robotic systems using ROS2 patterns
- Implement reliable inter-node communication
- Debug ROS2 systems using standard tools

---

### Module 2: Robot Kinematics and Motion Planning

*(Similar detailed breakdown for remaining 32 chapters...)*

**Note**: For brevity in this plan, I'll provide a condensed version of remaining modules. The full content-structure.md document will contain complete sub-section breakdowns for all 36 chapters.

#### Chapter 5: Forward Kinematics and Denavit-Hartenberg Convention
**Estimated Pages**: 15-18
**Sub-Sections**: Kinematic chains, DH parameters, FK computation, end-effector pose, singularities
**Practical Session**: Implementing Forward Kinematics (4 hours)

#### Chapter 6: Inverse Kinematics and Numerical Solutions
**Estimated Pages**: 18-20
**Sub-Sections**: Analytical vs numerical IK, Jacobian matrix, iterative methods, redundancy resolution
**Practical Session**: IK Solvers for Humanoid Arms (5 hours)

#### Chapter 7: Trajectory Planning and Interpolation
**Estimated Pages**: 14-16
**Sub-Sections**: Point-to-point motion, polynomial trajectories, splines, constraints, time-optimal
**Practical Session**: Smooth Trajectory Generation (4 hours)

#### Chapter 8: Path and Motion Planning Algorithms
**Estimated Pages**: 16-18
**Sub-Sections**: Configuration space, RRT/RRT*/PRM, A*/D*, potential fields, humanoid navigation
**Practical Session**: Implementing RRT Planner (5 hours)

#### Chapter 9: Whole-Body Motion Control
**Estimated Pages**: 18-22
**Sub-Sections**: Task prioritization, operational space control, whole-body IK, contact-aware planning
**Lab Activity**: Full-Body Motion Control Lab (6 hours)

---

### Module 3: Robot Dynamics and Control Systems

#### Chapter 10: Rigid Body Dynamics and Equations of Motion
**Estimated Pages**: 16-20
**Sub-Sections**: Newton-Euler, Lagrangian mechanics, mass matrix/Coriolis/gravity, recursive algorithms
**Practical Session**: Computing Robot Dynamics (4 hours)

#### Chapter 11: Fundamentals of Control Theory
**Estimated Pages**: 18-20
**Sub-Sections**: PID control, state-space, stability analysis, feedforward/feedback, digital control
**Practical Session**: PID Controller Design and Tuning (4 hours)

#### Chapter 12: Advanced Control Methods
**Estimated Pages**: 16-18
**Sub-Sections**: Computed torque, impedance/admittance, sliding mode, adaptive control, MPC basics
**Practical Session**: Implementing Computed Torque Control (5 hours)

#### Chapter 13: Force Control and Physical Interaction
**Estimated Pages**: 14-16
**Sub-Sections**: Force sensing, hybrid position/force control, compliance, contact stability, HRI
**Lab Activity**: Contact-Rich Manipulation Lab (5 hours)

#### Chapter 14: Real-Time Control Systems
**Estimated Pages**: 15-18
**Sub-Sections**: RTOS, timing/jitter, priority scheduling, hardware interfaces, safety monitoring
**Practical Session**: Real-Time ROS2 Control (4 hours)

---

### Module 4: Perception and Sensor Processing

#### Chapter 15: Computer Vision Fundamentals
**Estimated Pages**: 16-18
**Sub-Sections**: Image formation, processing operations, feature detection/description, stereo vision, calibration
**Practical Session**: Vision Processing with OpenCV (5 hours)

#### Chapter 16: Object Detection and Recognition
**Estimated Pages**: 18-20
**Sub-Sections**: Classical methods, deep learning (YOLO/Faster R-CNN), 3D detection/pose estimation, segmentation
**Practical Session**: Deep Learning Object Detection (6 hours)

#### Chapter 17: Simultaneous Localization and Mapping (SLAM)
**Estimated Pages**: 20-24
**Sub-Sections**: SLAM formulation, visual SLAM, lidar SLAM, graph-based optimization, loop closure
**Lab Activity**: Visual SLAM Implementation (6 hours)

#### Chapter 18: Multi-Sensor Fusion and State Estimation
**Estimated Pages**: 16-20
**Sub-Sections**: Kalman filtering, EKF, UKF, particle filters, IMU integration, fusion architectures
**Practical Session**: IMU-Vision Fusion (5 hours)

#### Chapter 19: 3D Point Cloud Processing
**Estimated Pages**: 14-16
**Sub-Sections**: Representation, filtering/downsampling, normal estimation, registration (ICP/NDT), segmentation
**Practical Session**: Point Cloud Processing Pipeline (4 hours)

---

### Module 5: Bipedal Locomotion and Balance

#### Chapter 20: Fundamentals of Bipedal Locomotion
**Estimated Pages**: 16-18
**Sub-Sections**: Gait cycles, ZMP, stability (static/dynamic), inverted pendulum, energy efficiency
**Practical Session**: Analyzing Humanoid Gait (4 hours)

#### Chapter 21: Walking Pattern Generation
**Estimated Pages**: 18-22
**Sub-Sections**: ZMP-based walking, preview control, capture point, trajectory generation, step adjustment
**Practical Session**: Implementing Walking Controller (6 hours)

#### Chapter 22: Balance and Push Recovery
**Estimated Pages**: 16-18
**Sub-Sections**: Ankle/hip/step strategies, momentum-based control, push recovery, terrain adaptation, multi-contact
**Lab Activity**: Balance and Recovery Lab (6 hours)

#### Chapter 23: Locomotion on Uneven Terrain
**Estimated Pages**: 14-16
**Sub-Sections**: Terrain perception, footstep planning, compliance control, stair climbing, slopes
**Practical Session**: Rough Terrain Navigation (5 hours)

#### Chapter 24: Advanced Locomotion: Running and Jumping
**Estimated Pages**: 12-14
**Sub-Sections**: Dynamic vs quasi-static, flight phase dynamics, landing control, energy storage/release, optimization
**Practical Session**: Implementing Jump Controller (3 hours)

---

### Module 6: AI and Machine Learning for Robotics

#### Chapter 25: Machine Learning Foundations for Robotics
**Estimated Pages**: 16-18
**Sub-Sections**: Supervised learning, neural networks/deep learning, training/validation, overfitting/regularization, transfer learning
**Practical Session**: Training Neural Networks for Robot Control (5 hours)

#### Chapter 26: Reinforcement Learning Fundamentals
**Estimated Pages**: 18-20
**Sub-Sections**: MDPs, value functions/Bellman equations, Q-learning/SARSA, policy gradient, actor-critic
**Practical Session**: RL for Simple Robot Tasks (5 hours)

#### Chapter 27: Deep Reinforcement Learning
**Estimated Pages**: 20-24
**Sub-Sections**: DQN, PPO, SAC, experience replay/exploration, sim-to-real transfer
**Lab Activity**: Training Humanoid with Deep RL (8 hours)

#### Chapter 28: Imitation Learning and Learning from Demonstration
**Estimated Pages**: 16-18
**Sub-Sections**: Behavioral cloning, inverse RL, GAIL, human demonstrations, data efficiency/augmentation
**Practical Session**: Behavioral Cloning for Manipulation (5 hours)

#### Chapter 29: Model-Based RL and World Models
**Estimated Pages**: 16-18
**Sub-Sections**: Learning dynamics models, planning with learned models, MPC with learned models, uncertainty quantification, hybrid approaches
**Practical Session**: Learning Robot Dynamics Models (5 hours)

---

### Module 7: Human-Robot Interaction and Collaboration

#### Chapter 30: Foundations of Human-Robot Interaction
**Estimated Pages**: 14-16
**Sub-Sections**: HRI design principles/UX, social robotics, safety/trust, interaction modalities, evaluation methods
**Practical Session**: Designing HRI Behaviors (4 hours)

#### Chapter 31: Speech Recognition and Natural Language Processing
**Estimated Pages**: 16-18
**Sub-Sections**: Speech recognition systems, NLU, dialog management, text-to-speech, intent recognition/slot filling
**Practical Session**: Voice-Controlled Robot Interface (5 hours)

#### Chapter 32: Gesture and Activity Recognition
**Estimated Pages**: 14-16
**Sub-Sections**: Body pose estimation (OpenPose/MediaPipe), gesture classification, activity recognition, real-time processing, context-aware interaction
**Lab Activity**: Gesture-Based Robot Control (6 hours)

#### Chapter 33: Collaborative Task Execution
**Estimated Pages**: 14-16
**Sub-Sections**: Shared autonomy/human-in-the-loop, intent prediction/proactive assistance, handover/object exchange, coordination/timing, safety monitoring
**Practical Session**: Implementing Handover Behavior (5 hours)

---

### Module 8: System Integration and Capstone Projects

#### Chapter 34: Full-Stack Robotics System Architecture
**Estimated Pages**: 18-20
**Sub-Sections**: Perception-planning-control pipeline, software architecture patterns, state machines/behavior trees, error handling/fault tolerance, performance optimization/profiling
**Practical Session**: Designing Complete Robot System (5 hours)

#### Chapter 35: Testing, Validation, and Safety
**Estimated Pages**: 16-18
**Sub-Sections**: Unit testing for robotics, integration testing/CI/CD, simulation-based testing, safety certification/standards, failure mode analysis
**Practical Session**: Implementing Robot Testing Framework (4 hours)

#### Chapter 36: Ethics, Safety, and Future of Humanoid Robotics
**Estimated Pages**: 14-16
**Sub-Sections**: Ethical considerations in AI/robotics, privacy/data security, job displacement/societal impact, regulations/policy frameworks, future trends/research directions
**Practical Session**: Case Study Analysis (3 hours)

#### Capstone Project 1: Autonomous Service Robot
**Estimated Pages**: 10-12 (project guide)
**Deliverables**: ROS2 system architecture, working simulation, technical documentation, video demonstration
**Estimated Time**: 15 hours

#### Capstone Project 2: Learning-Based Bipedal Walker
**Estimated Pages**: 10-12 (project guide)
**Deliverables**: Trained RL policy, training analysis/metrics, performance evaluation report, video demonstrations
**Estimated Time**: 12 hours

#### Capstone Project 3: Collaborative Assembly Robot
**Estimated Pages**: 10-12 (project guide)
**Deliverables**: Perception/manipulation pipeline, safety-certified behaviors, user study results, complete system demonstration
**Estimated Time**: 13 hours

---

## 4. Practical Labs and Projects

### Practical Sessions (36 total, one per chapter)

Each chapter includes either a **Practical Session** (3-6 hours) or **Lab Activity** (5-8 hours). All sessions follow the clarified approach (Q1): **Complete, runnable code with scaffolding and step-by-step modification instructions**.

**Format for Each Practical Session**:
1. **Learning Objectives** (what students will achieve)
2. **Prerequisites** (prior knowledge/software required)
3. **Setup Instructions** (environment, dependencies, downloads)
4. **Complete Code Solution** (fully functional starting point)
5. **Guided Exercises** (step-by-step modifications and extensions)
6. **Challenge Problems** (optional advanced exercises)
7. **Verification and Testing** (how to confirm success)
8. **Troubleshooting Guide** (common issues and solutions)

**Example Session Structure** (Chapter 1):

**Lab 01: Environment Setup and First ROS2 Node**

*Objectives*: Install ROS2 Humble, create workspace, run publisher/subscriber nodes, understand ROS2 graph

*Prerequisites*: Ubuntu 22.04 or Docker, basic command line skills

*Setup*:
```bash
# Provided installation script
./scripts/install-ros2-humble.sh
```

*Complete Code* (ros2_first_pkg/):
```python
# publisher.py - Complete working publisher
# subscriber.py - Complete working subscriber
# CMakeLists.txt - Build configuration
```

*Guided Exercises*:
1. Modify message type from String to custom message
2. Add parameter for publish rate
3. Create second subscriber with different callback
4. Implement basic message filtering

*Challenge*: Create bidirectional communication with request-response pattern

*Verification*: Run automated tests, visualize in rqt_graph

---

### Major Lab Activities (9 total)

Chapters with **Lab Activity** designations provide extended, integrative hands-on work:

1. **Lab 09**: Full-Body Motion Control Lab (Module 2, 6 hours)
2. **Lab 13**: Contact-Rich Manipulation Lab (Module 3, 5 hours)
3. **Lab 17**: Visual SLAM Implementation (Module 4, 6 hours)
4. **Lab 22**: Balance and Recovery Lab (Module 5, 6 hours)
5. **Lab 27**: Training Humanoid with Deep RL (Module 6, 8 hours)
6. **Lab 32**: Gesture-Based Robot Control (Module 7, 6 hours)

Each lab activity integrates concepts from multiple chapters and represents a significant milestone in skill development.

---

### Capstone Projects (3 projects, Module 8)

**Purpose**: Demonstrate comprehensive mastery by integrating multiple modules' concepts into a complete, working robotic system.

**Project 1: Autonomous Service Robot**
- **Required Modules**: 1, 2, 3, 4, 7
- **Objectives**:
  - Integrate perception, planning, and control systems
  - Implement SLAM for autonomous navigation
  - Add manipulation capabilities for object handling
  - Create natural human-robot interaction interface
- **Estimated Time**: 15 hours
- **Deliverables**:
  - Complete ROS2 system architecture
  - Working simulation demonstration
  - Technical documentation (architecture diagrams, API documentation)
  - Video demonstration of capabilities

**Project 2: Learning-Based Bipedal Walker**
- **Required Modules**: 2, 3, 5, 6
- **Objectives**:
  - Design and implement RL training pipeline
  - Create reward function for stable locomotion
  - Train policy in simulation environment
  - Evaluate performance on various terrains
- **Estimated Time**: 12 hours
- **Deliverables**:
  - Trained RL policy
  - Training analysis and metrics (learning curves, convergence analysis)
  - Performance evaluation report
  - Video of walking demonstrations on different terrains

**Project 3: Collaborative Assembly Robot**
- **Required Modules**: 2, 3, 4, 7
- **Objectives**:
  - Implement vision-based object detection and pose estimation
  - Design force-controlled manipulation behaviors
  - Create safe human-robot collaboration protocols
  - Integrate multimodal interaction (speech, gesture, force)
- **Estimated Time**: 13 hours
- **Deliverables**:
  - Perception and manipulation pipeline
  - Safety-certified interaction behaviors
  - User study results (if feasible)
  - Complete system demonstration

**Capstone Grading Rubric** (from assessmentPlan):
- System design and architecture: 20%
- Implementation quality and completeness: 30%
- Innovation and problem-solving: 15%
- Documentation and presentation: 15%
- Demonstration and testing: 20%

---

## 5. Tools, Libraries, and Robotics Hardware

### Software Development Tools

**Primary Development Environment**:
- **Operating System**: Ubuntu 22.04 LTS (Jammy Jellyfish)
- **Docker**: For containerized development (Windows/Mac alternative)
- **IDE/Editors**: VS Code (recommended), PyCharm Professional
- **Version Control**: Git 2.30+, GitHub for hosting

**Robotics Frameworks**:
- **ROS2 Humble Hawksbill (LTS)**: Core robotics middleware
  - rclpy (Python client library)
  - rclcpp (C++ client library)
- **MoveIt2**: Motion planning framework
- **Nav2**: Navigation framework
- **ros2_control**: Hardware interface and controller management

**Simulation Environments**:
- **PyBullet**: Lightweight physics simulation (primary for quick prototyping)
- **Webots**: Commercial-grade robot simulator (visual quality, sensors)
- **MuJoCo**: Physics engine for continuous control (RL training)
- **Gazebo**: Integrated ROS2 simulation (comprehensive robot testing)

**Programming Languages**:
- **Python 3.10+**: Primary language for exercises and labs
  - NumPy, SciPy: Numerical computation
  - Matplotlib, Plotly: Data visualization
  - transforms3d: Transformation mathematics
- **C++17/20**: Performance-critical and embedded contexts
  - Eigen: Linear algebra library
  - Boost: General utilities

**AI/ML Frameworks**:
- **PyTorch 2.0+**: Deep learning (preferred for flexibility)
- **TensorFlow 2.x**: Neural networks (compatibility)
- **Stable-Baselines3**: Reinforcement learning algorithms
- **OpenAI Gym / Gymnasium**: RL environments

**Computer Vision Libraries**:
- **OpenCV 4.x**: Image processing and computer vision
- **MediaPipe**: Pose estimation and gesture recognition
- **YOLO (YOLOv8)**: Object detection
- **Open3D**: Point cloud processing
- **PCL (Point Cloud Library)**: Advanced 3D processing

**Control and Dynamics Libraries**:
- **Pinocchio**: Rigid body dynamics computations
- **OMPL (Open Motion Planning Library)**: Motion planning algorithms
- **control (Python)**: Control systems analysis and design

**Development and Deployment Tools**:
- **Docker Desktop**: Container management
- **GitHub Actions**: CI/CD pipeline
- **RViz2**: ROS2 visualization
- **rqt**: ROS2 debugging and monitoring tools
- **Jupyter Notebook**: Interactive exploration (optional)

---

### Recommended Hardware

**Minimum Requirements** (for all exercises):
- **CPU**: Intel Core i5 or AMD Ryzen 5 (quad-core)
- **RAM**: 8 GB
- **GPU**: Integrated graphics (limited deep learning capability)
- **Storage**: 50 GB free space
- **OS**: Ubuntu 22.04 LTS (native or VM) or Docker on Windows/Mac

**Recommended Configuration** (optimal experience):
- **CPU**: Intel Core i7/i9 or AMD Ryzen 7/9 (8+ cores)
- **RAM**: 16-32 GB
- **GPU**: NVIDIA GPU with 6+ GB VRAM (RTX 3060 or better) for deep learning
- **Storage**: 100 GB SSD free space
- **OS**: Ubuntu 22.04 LTS (native installation preferred)

**Optional Physical Hardware** (for enrichment, not required):

1. **Low-cost Robot Arm Kit** ($150-$500)
   - Purpose: Hands-on experience with real hardware
   - Examples: Freenove Robot Arm, MyCobot 280, Lynxmotion AL5D
   - Use cases: Testing FK/IK algorithms, control tuning, trajectory execution

2. **USB Camera** ($50-$200)
   - Purpose: Testing computer vision algorithms with real sensors
   - Examples: Logitech C920, Intel RealSense D435 (depth camera)
   - Use cases: Object detection, SLAM, visual servoing

3. **Arduino/Raspberry Pi** ($35-$80)
   - Purpose: Experimenting with embedded control and sensor integration
   - Examples: Arduino Mega, Raspberry Pi 4
   - Use cases: Low-level motor control, sensor interfacing, real-time constraints

4. **IMU Sensor** ($20-$50)
   - Purpose: Testing sensor fusion algorithms
   - Examples: MPU6050, BNO055
   - Use cases: Orientation estimation, Kalman filtering

**Cloud Alternatives** (if local hardware insufficient):
- **Google Colab Pro**: GPU-accelerated deep learning ($10/month)
- **AWS EC2 instances**: Intensive simulations (pay-as-you-go)
- **GitHub Codespaces**: Cloud-based development (free tier available)

---

### Datasets and Resources

**Required Datasets**:

1. **COCO (Common Objects in Context)**
   - Purpose: Object detection and segmentation training
   - Size: ~25 GB (full dataset)
   - URL: https://cocodataset.org/

2. **ImageNet**
   - Purpose: Pre-trained models and transfer learning
   - Size: Variable (pre-trained models ~100-500 MB)
   - URL: https://www.image-net.org/

3. **TUM RGB-D Dataset**
   - Purpose: SLAM and visual odometry evaluation
   - Size: ~10 GB
   - URL: https://vision.in.tum.de/data/datasets/rgbd-dataset

4. **RoboCup@Home Dataset**
   - Purpose: Domestic service robot scenarios
   - Size: Variable
   - URL: https://athome.robocup.org/

5. **DexNet**
   - Purpose: Grasping and manipulation training data
   - Size: ~50 GB
   - URL: https://berkeleyautomation.github.io/dex-net/

**Simulation Assets**:

1. **PyBullet Robot Models**
   - Pre-built URDF models for humanoid robots
   - Source: Built-in PyBullet data, community repositories

2. **Webots Robot Library**
   - Official robot models for Webots
   - Source: Webots installation, official repository

3. **MuJoCo Humanoid Models**
   - Physics-accurate humanoid models
   - Source: MuJoCo model library, DeepMind repositories

**Supplementary Resources**:

1. **Documentation**:
   - ROS2 Official Documentation: https://docs.ros.org/en/humble/
   - PyTorch Documentation: https://pytorch.org/docs/
   - OpenCV Documentation: https://docs.opencv.org/

2. **Books** (recommended reading):
   - "Modern Robotics: Mechanics, Planning, and Control" by Lynch & Park
   - "Probabilistic Robotics" by Thrun, Burgard, and Fox
   - "Deep Learning" by Goodfellow, Bengio, and Courville

3. **Online Courses**:
   - MIT OpenCourseWare - Underactuated Robotics: https://underactuated.mit.edu/
   - Stanford CS231n - Convolutional Neural Networks
   - Berkeley CS285 - Deep Reinforcement Learning

4. **Research Papers** (curated selection per module):
   - Deep Reinforcement Learning for Bipedal Walking (Module 6)
   - Whole-Body Control of Humanoid Robots (Module 2)
   - Visual SLAM for Mobile Robots (Module 4)

---

## 6. Learning Progression Roadmap

The course follows a carefully designed progression that builds knowledge incrementally, ensuring each module provides the foundation for subsequent modules.

### Progression Principles

1. **Foundational First**: Mathematical and software foundations before advanced topics
2. **Theory-Practice Integration**: Each theoretical concept immediately followed by hands-on lab
3. **Incremental Complexity**: Start with simple systems, gradually add complexity
4. **Spiraling Curriculum**: Revisit concepts at increasing depth levels
5. **Integration Milestones**: Major labs integrate multiple concepts at module boundaries

---

### Week-by-Week Progression (12-16 week suggested timeline)

**Weeks 1-2: Module 1 - Foundations**
- **Week 1**: Chapters 1-2
  - Understand physical AI concepts
  - Master mathematical foundations
  - Set up development environment
  - First ROS2 programs
- **Week 2**: Chapters 3-4
  - Learn robot anatomy
  - Master ROS2 architecture
  - Build multi-node systems
  - **Milestone**: Functional ROS2 development environment

**Weeks 3-4: Module 2 - Kinematics (Part 1)**
- **Week 3**: Chapters 5-6
  - Forward kinematics with DH convention
  - Inverse kinematics algorithms
  - Jacobian-based methods
- **Week 4**: Chapters 7-9
  - Trajectory planning and interpolation
  - Motion planning algorithms (RRT, RRT*)
  - Whole-body control introduction
  - **Milestone**: Lab 09 - Full-Body Motion Control

**Weeks 5-6: Module 3 - Dynamics and Control**
- **Week 5**: Chapters 10-12
  - Rigid body dynamics
  - PID control and tuning
  - Advanced control methods
- **Week 6**: Chapters 13-14
  - Force control and physical interaction
  - Real-time control systems
  - **Milestone**: Lab 13 - Contact-Rich Manipulation

**Weeks 7-8: Module 4 - Perception**
- **Week 7**: Chapters 15-16
  - Computer vision fundamentals
  - Object detection with deep learning
  - 3D pose estimation
- **Week 8**: Chapters 17-19
  - SLAM implementation
  - Sensor fusion and state estimation
  - Point cloud processing
  - **Milestone**: Lab 17 - Visual SLAM Implementation

**Weeks 9-10: Module 5 - Bipedal Locomotion**
- **Week 9**: Chapters 20-22
  - Bipedal locomotion fundamentals
  - Walking pattern generation
  - Balance control and push recovery
  - **Milestone**: Lab 22 - Balance and Recovery
- **Week 10**: Chapters 23-24
  - Terrain locomotion
  - Running and jumping

**Weeks 11-12: Module 6 - AI and Machine Learning**
- **Week 11**: Chapters 25-26
  - ML foundations for robotics
  - Reinforcement learning fundamentals
  - Q-learning and policy gradients
- **Week 12**: Chapters 27-29
  - Deep reinforcement learning
  - Imitation learning
  - Model-based RL
  - **Milestone**: Lab 27 - Training Humanoid with Deep RL

**Week 13: Module 7 - Human-Robot Interaction**
- Chapters 30-33
  - HRI fundamentals
  - Speech recognition and NLP
  - Gesture recognition
  - Collaborative task execution
  - **Milestone**: Lab 32 - Gesture-Based Robot Control

**Weeks 14-16: Module 8 - Integration and Capstone**
- **Week 14**: Chapters 34-36
  - System architecture design
  - Testing and validation
  - Ethics and future directions
- **Weeks 15-16**: Capstone Projects
  - Select one of three capstone projects
  - Complete implementation
  - Documentation and presentation
  - **Final Milestone**: Capstone project demonstration

---

### Skill Progression Matrix

| Module | New Skills Acquired | Prerequisites from Prior Modules | Preparation for Future Modules |
|--------|--------------------|---------------------------------|--------------------------------|
| 1: Foundations | Math, ROS2, Robot anatomy | Python, C++, Linux, Linear algebra | Provides foundation for all subsequent modules |
| 2: Kinematics | FK/IK, Trajectory planning, Motion planning | Module 1: Math, ROS2 | Modules 3 (dynamics uses kinematics), 5 (locomotion needs motion planning) |
| 3: Dynamics & Control | Dynamics computation, Control design, Real-time systems | Modules 1-2: Math, kinematics | Modules 5 (locomotion control), 6 (RL needs dynamics) |
| 4: Perception | Computer vision, SLAM, Sensor fusion | Module 1: Math, ROS2 | Module 7 (HRI uses vision), Module 8 (integration needs perception) |
| 5: Locomotion | Bipedal walking, Balance, Terrain navigation | Modules 1-3: Kinematics, dynamics, control | Module 6 (RL applied to locomotion), Module 8 (integration) |
| 6: AI & Learning | ML, RL, Deep RL, Imitation learning | Modules 1-5: All foundations | Module 8 (integration and advanced projects) |
| 7: HRI | Speech/NLP, Gesture recognition, Collaboration | Module 4: Computer vision; Module 1: ROS2 | Module 8 (integration in service robot project) |
| 8: Integration | System architecture, Testing, Ethics | Modules 1-7: All skills | Capstone projects demonstrate comprehensive mastery |

---

## 7. Approximate Page Count for Each Module

**Methodology**: Based on specification estimate of 100,000-150,000 total words across 36 chapters:
- Average: 125,000 words / 36 chapters = 3,472 words/chapter
- Academic textbook format: ~400-450 words/page
- Average pages per chapter: 8-10 pages
- Adjustments based on complexity and practical content

### Module 1: Foundations of Physical AI and Robotics
**Total Estimated Pages**: 60-73

| Chapter | Title | Pages | Words |
|---------|-------|-------|-------|
| 1 | Introduction to Physical AI | 12-15 | 5,000-6,500 |
| 2 | Mathematical Foundations | 18-22 | 7,500-9,500 |
| 3 | Robot Anatomy and Components | 14-16 | 5,500-7,000 |
| 4 | ROS2 Architecture | 16-20 | 6,500-8,500 |

### Module 2: Robot Kinematics and Motion Planning
**Total Estimated Pages**: 81-94

| Chapter | Title | Pages | Words |
|---------|-------|-------|-------|
| 5 | Forward Kinematics and DH Convention | 15-18 | 6,000-7,500 |
| 6 | Inverse Kinematics | 18-20 | 7,000-8,500 |
| 7 | Trajectory Planning | 14-16 | 5,500-7,000 |
| 8 | Path and Motion Planning | 16-18 | 6,500-7,500 |
| 9 | Whole-Body Motion Control | 18-22 | 7,500-9,500 |

### Module 3: Robot Dynamics and Control Systems
**Total Estimated Pages**: 79-92

| Chapter | Title | Pages | Words |
|---------|-------|-------|-------|
| 10 | Rigid Body Dynamics | 16-20 | 6,500-8,500 |
| 11 | Fundamentals of Control Theory | 18-20 | 7,000-8,500 |
| 12 | Advanced Control Methods | 16-18 | 6,500-7,500 |
| 13 | Force Control | 14-16 | 5,500-7,000 |
| 14 | Real-Time Control Systems | 15-18 | 6,000-7,500 |

### Module 4: Perception and Sensor Processing
**Total Estimated Pages**: 80-94

| Chapter | Title | Pages | Words |
|---------|-------|-------|-------|
| 15 | Computer Vision Fundamentals | 16-18 | 6,500-7,500 |
| 16 | Object Detection and Recognition | 18-20 | 7,000-8,500 |
| 17 | SLAM | 20-24 | 8,500-10,500 |
| 18 | Multi-Sensor Fusion | 16-20 | 6,500-8,500 |
| 19 | Point Cloud Processing | 14-16 | 5,500-7,000 |

### Module 5: Bipedal Locomotion and Balance
**Total Estimated Pages**: 76-88

| Chapter | Title | Pages | Words |
|---------|-------|-------|-------|
| 20 | Fundamentals of Bipedal Locomotion | 16-18 | 6,500-7,500 |
| 21 | Walking Pattern Generation | 18-22 | 7,500-9,500 |
| 22 | Balance and Push Recovery | 16-18 | 6,500-7,500 |
| 23 | Locomotion on Uneven Terrain | 14-16 | 5,500-7,000 |
| 24 | Running and Jumping | 12-14 | 5,000-6,000 |

### Module 6: AI and Machine Learning for Robotics
**Total Estimated Pages**: 86-98

| Chapter | Title | Pages | Words |
|---------|-------|-------|-------|
| 25 | ML Foundations for Robotics | 16-18 | 6,500-7,500 |
| 26 | Reinforcement Learning Fundamentals | 18-20 | 7,000-8,500 |
| 27 | Deep Reinforcement Learning | 20-24 | 8,500-10,500 |
| 28 | Imitation Learning | 16-18 | 6,500-7,500 |
| 29 | Model-Based RL | 16-18 | 6,500-7,500 |

### Module 7: Human-Robot Interaction and Collaboration
**Total Estimated Pages**: 58-66

| Chapter | Title | Pages | Words |
|---------|-------|-------|-------|
| 30 | Foundations of HRI | 14-16 | 5,500-7,000 |
| 31 | Speech Recognition and NLP | 16-18 | 6,500-7,500 |
| 32 | Gesture and Activity Recognition | 14-16 | 5,500-7,000 |
| 33 | Collaborative Task Execution | 14-16 | 5,500-7,000 |

### Module 8: System Integration and Capstone Projects
**Total Estimated Pages**: 80-92

| Chapter | Title | Pages | Words |
|---------|-------|-------|-------|
| 34 | Full-Stack System Architecture | 18-20 | 7,000-8,500 |
| 35 | Testing, Validation, and Safety | 16-18 | 6,500-7,500 |
| 36 | Ethics and Future | 14-16 | 5,500-7,000 |
| Capstone 1 | Autonomous Service Robot | 10-12 | 4,000-5,000 |
| Capstone 2 | Learning-Based Bipedal Walker | 10-12 | 4,000-5,000 |
| Capstone 3 | Collaborative Assembly Robot | 10-12 | 4,000-5,000 |

---

### Total Course Length

**Main Content**: 600-697 pages (36 chapters)
**Capstone Projects**: 30-36 pages (3 projects)
**Supplementary Materials** (estimated):
- Prerequisites section: 30-40 pages
- Glossary: 10-12 pages
- Resources and references: 15-20 pages
- Assessment materials: 20-25 pages

**Grand Total**: ~705-830 pages

**Word Count**: 100,000-150,000 words (main content)
**Total with supplementary**: ~120,000-170,000 words

This aligns with the specification's estimate and represents a comprehensive professional textbook.

---

## 8. Docusaurus Folder Structure Plan

Based on clarification Q2 (hierarchical sidebar with modules as top-level categories, chapters as expandable sections, and auto-generated navigation), the Docusaurus structure will be organized as follows:

### Directory Structure

```
humanoid-robotics-course/           # Repository root
├── docs/                            # All course content (Markdown/MDX)
│   ├── index.md                    # Course homepage
│   ├── prerequisites/              # Prerequisites module
│   │   ├── index.md               # Prerequisites overview
│   │   ├── self-assessment.md
│   │   ├── python-refresher.md
│   │   ├── cpp-basics.md
│   │   ├── math-foundations.md
│   │   └── linux-setup.md
│   ├── module-01-foundations/
│   │   ├── index.md               # Module 1 overview
│   │   ├── ch01-intro-physical-ai.md
│   │   ├── ch02-math-foundations.md
│   │   ├── ch03-robot-anatomy.md
│   │   └── ch04-ros2-architecture.md
│   ├── module-02-kinematics/
│   │   ├── index.md
│   │   ├── ch05-forward-kinematics.md
│   │   ├── ch06-inverse-kinematics.md
│   │   ├── ch07-trajectory-planning.md
│   │   ├── ch08-motion-planning.md
│   │   └── ch09-whole-body-control.md
│   ├── module-03-dynamics-control/
│   │   └── ... (5 chapters)
│   ├── module-04-perception/
│   │   └── ... (5 chapters)
│   ├── module-05-locomotion/
│   │   └── ... (5 chapters)
│   ├── module-06-ai-learning/
│   │   └── ... (5 chapters)
│   ├── module-07-hri/
│   │   └── ... (4 chapters)
│   ├── module-08-integration/
│   │   ├── index.md
│   │   ├── ch34-system-architecture.md
│   │   ├── ch35-testing-validation.md
│   │   ├── ch36-ethics-future.md
│   │   ├── capstone-project-1.md
│   │   ├── capstone-project-2.md
│   │   └── capstone-project-3.md
│   ├── labs/                       # Hands-on lab guides
│   │   ├── lab-01-environment-setup/
│   │   │   ├── index.md
│   │   │   ├── setup-instructions.md
│   │   │   ├── code-walkthrough.md
│   │   │   └── exercises.md
│   │   ├── lab-02-transformation-math/
│   │   └── ... (36 labs total)
│   ├── code-examples/              # Code example documentation
│   │   ├── index.md
│   │   ├── module-01/
│   │   │   ├── ros2-pub-sub.md
│   │   │   ├── rotation-matrices.md
│   │   │   └── ...
│   │   └── ... (per module)
│   ├── resources/
│   │   ├── datasets.md
│   │   ├── tools-setup.md
│   │   ├── hardware-guide.md
│   │   ├── troubleshooting.md
│   │   ├── research-papers.md
│   │   └── external-resources.md
│   ├── assessments/
│   │   ├── quizzes/
│   │   │   ├── module-01-quiz.md
│   │   │   └── ... (8 quizzes)
│   │   └── rubrics/
│   │       ├── lab-report-rubric.md
│   │       └── capstone-rubric.md
│   ├── glossary.md
│   ├── faq.md
│   └── about.md
│
├── static/                         # Static assets
│   ├── img/
│   │   ├── robots/                # Robot photos
│   │   ├── diagrams/              # Technical diagrams (PNG/SVG)
│   │   ├── screenshots/           # Software screenshots
│   │   └── visualizations/        # Data visualizations
│   ├── models/                    # URDF models, meshes
│   │   ├── humanoid-simple/
│   │   ├── humanoid-atlas/
│   │   └── environments/
│   └── downloads/
│       ├── code-archives/         # Zipped code per module
│       └── datasets/              # Mirrored datasets
│
├── src/                           # Custom Docusaurus components
│   ├── components/
│   │   ├── Quiz.js               # Automated quiz component
│   │   ├── ProgressTracker.js    # Progress tracking
│   │   ├── CodeBlock.js          # Enhanced code blocks
│   │   └── DiagramRenderer.js    # Mermaid renderer
│   ├── css/
│   │   └── custom.css            # Custom styling
│   └── pages/
│       └── index.js              # Custom landing page
│
├── code/                          # Actual code examples (separate from docs)
│   ├── module-01/
│   │   ├── ch01-ros2-pub-sub/
│   │   │   ├── README.md
│   │   │   ├── publisher.py
│   │   │   ├── subscriber.py
│   │   │   ├── package.xml
│   │   │   └── CMakeLists.txt
│   │   ├── ch02-rotation-matrices/
│   │   └── ...
│   ├── module-02/
│   └── ... (code for all modules)
│
├── docusaurus.config.js           # Docusaurus configuration
├── sidebars.js                    # Sidebar configuration
├── package.json                   # Node.js dependencies
├── .github/
│   └── workflows/
│       └── deploy.yml            # GitHub Actions CI/CD
└── README.md                      # Repository README
```

---

### Sidebar Configuration (sidebars.js)

The sidebar will be configured to create the hierarchical structure per clarification Q2:

```javascript
module.exports = {
  courseSidebar: [
    {
      type: 'doc',
      id: 'index',
      label: 'Course Home',
    },
    {
      type: 'category',
      label: 'Prerequisites',
      collapsed: false,
      items: [
        'prerequisites/index',
        'prerequisites/self-assessment',
        'prerequisites/python-refresher',
        'prerequisites/cpp-basics',
        'prerequisites/math-foundations',
        'prerequisites/linux-setup',
      ],
    },
    {
      type: 'category',
      label: 'Module 1: Foundations of Physical AI',
      collapsed: true,
      link: {
        type: 'doc',
        id: 'module-01-foundations/index',
      },
      items: [
        'module-01-foundations/ch01-intro-physical-ai',
        'module-01-foundations/ch02-math-foundations',
        'module-01-foundations/ch03-robot-anatomy',
        'module-01-foundations/ch04-ros2-architecture',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: Robot Kinematics',
      collapsed: true,
      link: {
        type: 'doc',
        id: 'module-02-kinematics/index',
      },
      items: [
        'module-02-kinematics/ch05-forward-kinematics',
        'module-02-kinematics/ch06-inverse-kinematics',
        'module-02-kinematics/ch07-trajectory-planning',
        'module-02-kinematics/ch08-motion-planning',
        'module-02-kinematics/ch09-whole-body-control',
      ],
    },
    // ... (similar structure for modules 3-8)
    {
      type: 'category',
      label: 'Hands-On Labs',
      collapsed: true,
      items: [
        'labs/lab-01-environment-setup/index',
        'labs/lab-02-transformation-math/index',
        // ... (all 36 labs)
      ],
    },
    {
      type: 'category',
      label: 'Code Examples',
      collapsed: true,
      items: [
        'code-examples/index',
        {
          type: 'category',
          label: 'Module 1 Examples',
          items: [
            'code-examples/module-01/ros2-pub-sub',
            // ... (all module 1 examples)
          ],
        },
        // ... (similar for all modules)
      ],
    },
    {
      type: 'category',
      label: 'Resources',
      items: [
        'resources/datasets',
        'resources/tools-setup',
        'resources/hardware-guide',
        'resources/troubleshooting',
        'resources/research-papers',
        'resources/external-resources',
      ],
    },
    {
      type: 'category',
      label: 'Assessments',
      items: [
        {
          type: 'category',
          label: 'Quizzes',
          items: [
            'assessments/quizzes/module-01-quiz',
            // ... (all module quizzes)
          ],
        },
        {
          type: 'category',
          label: 'Rubrics',
          items: [
            'assessments/rubrics/lab-report-rubric',
            'assessments/rubrics/capstone-rubric',
          ],
        },
      ],
    },
    {
      type: 'doc',
      id: 'glossary',
      label: 'Glossary',
    },
    {
      type: 'doc',
      id: 'faq',
      label: 'FAQ',
    },
    {
      type: 'doc',
      id: 'about',
      label: 'About',
    },
  ],
};
```

**Key Features**:
- **Hierarchical Structure**: Modules as top-level categories
- **Expandable Sections**: Chapters within each module
- **Auto-Generated Navigation**: Docusaurus provides prev/next buttons automatically
- **Collapsible Categories**: Students can expand/collapse modules for focused navigation
- **Dedicated Sections**: Separate categories for labs, code examples, resources, assessments

---

### Docusaurus Configuration (docusaurus.config.js)

```javascript
module.exports = {
  title: 'Physical AI & Humanoid Robotics Course',
  tagline: 'Master intelligent humanoid robotics through hands-on simulation and real-world applications',
  url: 'https://your-org.github.io',
  baseUrl: '/humanoid-robotics-course/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  organizationName: 'your-org',
  projectName: 'humanoid-robotics-course',

  themeConfig: {
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'Course Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'index',
          position: 'left',
          label: 'Course',
        },
        {
          to: '/labs',
          label: 'Labs',
          position: 'left',
        },
        {
          to: '/code-examples',
          label: 'Code Examples',
          position: 'left',
        },
        {
          to: '/resources',
          label: 'Resources',
          position: 'left',
        },
        {
          href: 'https://github.com/your-org/humanoid-robotics-course',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Course',
          items: [
            {label: 'Getting Started', to: '/docs'},
            {label: 'Prerequisites', to: '/docs/prerequisites'},
            {label: 'Modules', to: '/docs/module-01-foundations'},
          ],
        },
        {
          title: 'Resources',
          items: [
            {label: 'Datasets', to: '/docs/resources/datasets'},
            {label: 'Tools Setup', to: '/docs/resources/tools-setup'},
            {label: 'Troubleshooting', to: '/docs/resources/troubleshooting'},
          ],
        },
        {
          title: 'Community',
          items: [
            {label: 'GitHub', href: 'https://github.com/your-org/humanoid-robotics-course'},
            {label: 'Discussions', href: 'https://github.com/your-org/humanoid-robotics-course/discussions'},
            {label: 'Issues', href: 'https://github.com/your-org/humanoid-robotics-course/issues'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Course Development Team. Licensed under CC BY-NC-SA 4.0.`,
    },
    prism: {
      theme: require('prism-react-renderer/themes/github'),
      darkTheme: require('prism-react-renderer/themes/dracula'),
      additionalLanguages: ['python', 'cpp', 'bash', 'yaml', 'json'],
    },
    algolia: {  // Search functionality (FR-013)
      appId: 'YOUR_APP_ID',
      apiKey: 'YOUR_API_KEY',
      indexName: 'humanoid-robotics-course',
      contextualSearch: true,
    },
  },

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/your-org/humanoid-robotics-course/edit/main/',
          remarkPlugins: [require('remark-math')],
          rehypePlugins: [require('rehype-katex')],
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'labs',
        path: 'labs',
        routeBasePath: 'labs',
        sidebarPath: require.resolve('./sidebars.js'),
      },
    ],
  ],

  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
      type: 'text/css',
      integrity: 'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
      crossorigin: 'anonymous',
    },
  ],
};
```

**Key Configuration Features**:
- **Responsive Design**: Mobile-first theme (FR-012)
- **Search**: Algolia DocSearch integration (FR-013, SC-012)
- **Math Support**: KaTeX for mathematical equations (aligned with clarification Q3)
- **Code Highlighting**: Prism with Python, C++, YAML support
- **Multiple Docs Plugins**: Separate sections for main docs and labs
- **Edit on GitHub**: Easy contribution workflow
- **Dark Mode**: Built-in theme switching

---

## 9. Milestone Timeline

The development timeline is organized into phases, each with clear deliverables and dependencies.

### Phase 0: Project Setup and Infrastructure (Weeks 1-2)

**Duration**: 2 weeks
**Team**: 1-2 developers + 1 technical writer

**Milestones**:
- **M0.1**: Repository initialization and Docusaurus setup
  - Create GitHub repository
  - Initialize Docusaurus project
  - Configure sidebar and navigation
  - Set up CI/CD pipeline (GitHub Actions)
  - **Deliverable**: Empty Docusaurus site deployed to GitHub Pages

- **M0.2**: Content templates and style guide
  - Create chapter template
  - Create lab template
  - Create code example template
  - Define Mermaid diagram standards (per clarification Q5)
  - Establish writing style guide
  - **Deliverable**: Template library and style guide document

- **M0.3**: Development environment setup
  - Docker containers for ROS2 + simulation environments
  - Installation scripts for all tools
  - Validation scripts for setup
  - **Deliverable**: Tested installation guide and Docker images

---

### Phase 1: Module 1 - Foundations (Weeks 3-6)

**Duration**: 4 weeks
**Team**: 2-3 technical writers + 1 developer (code examples)

**Milestones**:
- **M1.1**: Chapter 1-2 complete (Week 3)
  - Write Chapters 1-2 content
  - Create Lab 01 (Environment Setup)
  - Create Lab 02 (Transformation Math)
  - Develop code examples
  - **Deliverable**: Chapters 1-2, Labs 01-02, Code examples

- **M1.2**: Chapter 3-4 complete (Week 4)
  - Write Chapters 3-4 content
  - Create Lab 03 (URDF Models)
  - Create Lab 04 (Multi-Node ROS2)
  - Develop code examples
  - **Deliverable**: Chapters 3-4, Labs 03-04, Code examples

- **M1.3**: Module 1 review and refinement (Week 5)
  - Technical review
  - Code testing on minimum hardware
  - Create Module 1 quiz (automated)
  - **Deliverable**: Complete, reviewed Module 1

- **M1.4**: Supplementary materials (Week 6)
  - Prerequisites section complete
  - Glossary terms for Module 1
  - Troubleshooting guide
  - **Deliverable**: Prerequisites, glossary, troubleshooting

---

### Phase 2: Module 2 - Kinematics (Weeks 7-11)

**Duration**: 5 weeks
**Team**: 2-3 technical writers + 1 developer

**Milestones**:
- **M2.1**: Chapters 5-6 complete (Weeks 7-8)
  - Forward and Inverse Kinematics content
  - Labs 05-06
  - Code examples
  - Mermaid diagrams for FK/IK processes
  - **Deliverable**: Chapters 5-6, Labs 05-06

- **M2.2**: Chapters 7-8 complete (Weeks 9-10)
  - Trajectory and Motion Planning content
  - Labs 07-08
  - RRT visualization diagrams
  - **Deliverable**: Chapters 7-8, Labs 07-08

- **M2.3**: Chapter 9 and integration (Week 11)
  - Whole-Body Control content
  - Lab 09 (major integration lab)
  - Module 2 quiz
  - **Deliverable**: Complete Module 2 with Lab 09

---

### Phase 3: Module 3 - Dynamics and Control (Weeks 12-16)

**Duration**: 5 weeks
**Team**: 2-3 technical writers + 1 developer

**Milestones**:
- **M3.1**: Chapters 10-11 complete (Weeks 12-13)
- **M3.2**: Chapters 12-13 complete (Weeks 14-15)
- **M3.3**: Chapter 14 and Lab 13 integration (Week 16)
- **Deliverable**: Complete Module 3 with Contact-Rich Manipulation Lab

---

### Phase 4: Module 4 - Perception (Weeks 17-22)

**Duration**: 6 weeks
**Team**: 3-4 technical writers + 1-2 developers (computer vision code)

**Milestones**:
- **M4.1**: Chapters 15-16 complete (Weeks 17-19)
  - Computer vision and object detection
  - Integration with YOLO, OpenCV
  - Labs 15-16
- **M4.2**: Chapters 17-18 complete (Weeks 20-21)
  - SLAM and sensor fusion
  - Lab 17 (Visual SLAM - major lab)
  - Lab 18
- **M4.3**: Chapter 19 and review (Week 22)
  - Point cloud processing
  - Lab 19
  - Module 4 quiz
- **Deliverable**: Complete Module 4 with Visual SLAM Lab

---

### Phase 5: Module 5 - Bipedal Locomotion (Weeks 23-28)

**Duration**: 6 weeks
**Team**: 2-3 technical writers + 1 developer

**Milestones**:
- **M5.1**: Chapters 20-21 complete (Weeks 23-25)
  - Bipedal fundamentals and walking
  - Labs 20-21
- **M5.2**: Chapters 22-23 complete (Weeks 26-27)
  - Balance control and terrain locomotion
  - Lab 22 (Balance and Recovery - major lab)
  - Lab 23
- **M5.3**: Chapter 24 and review (Week 28)
  - Running and jumping
  - Lab 24
  - Module 5 quiz
- **Deliverable**: Complete Module 5 with Balance and Recovery Lab

---

### Phase 6: Module 6 - AI and Machine Learning (Weeks 29-36)

**Duration**: 8 weeks
**Team**: 3-4 technical writers + 2 developers (RL/ML specialists)

**Milestones**:
- **M6.1**: Chapters 25-26 complete (Weeks 29-31)
  - ML foundations and basic RL
  - Labs 25-26
- **M6.2**: Chapter 27 complete (Weeks 32-34)
  - Deep RL (most complex chapter)
  - Lab 27 (Training Humanoid with Deep RL - major lab, 8 hours)
  - Extensive testing required
- **M6.3**: Chapters 28-29 and review (Weeks 35-36)
  - Imitation learning and model-based RL
  - Labs 28-29
  - Module 6 quiz
- **Deliverable**: Complete Module 6 with Deep RL Lab

---

### Phase 7: Module 7 - Human-Robot Interaction (Weeks 37-40)

**Duration**: 4 weeks
**Team**: 2-3 technical writers + 1 developer

**Milestones**:
- **M7.1**: Chapters 30-31 complete (Weeks 37-38)
  - HRI fundamentals and speech/NLP
  - Labs 30-31
- **M7.2**: Chapters 32-33 complete (Weeks 39-40)
  - Gesture recognition and collaboration
  - Lab 32 (Gesture-Based Robot Control - major lab)
  - Lab 33
  - Module 7 quiz
- **Deliverable**: Complete Module 7 with Gesture-Based Control Lab

---

### Phase 8: Module 8 - Integration and Capstone (Weeks 41-46)

**Duration**: 6 weeks
**Team**: 3-4 technical writers + 2 developers

**Milestones**:
- **M8.1**: Chapters 34-36 complete (Weeks 41-42)
  - System architecture, testing, ethics
  - Labs 34-36
- **M8.2**: Capstone Project 1 (Week 43)
  - Autonomous Service Robot guide
  - Starter code and scaffolding
- **M8.3**: Capstone Project 2 (Week 44)
  - Learning-Based Bipedal Walker guide
  - RL training infrastructure
- **M8.4**: Capstone Project 3 (Week 45)
  - Collaborative Assembly Robot guide
  - Vision + manipulation integration
- **M8.5**: Module 8 integration and review (Week 46)
  - Capstone rubric finalization
  - Module 8 quiz
  - Final testing
- **Deliverable**: Complete Module 8 with all 3 capstone projects

---

### Phase 9: Course-Wide Refinement (Weeks 47-50)

**Duration**: 4 weeks
**Team**: Full team

**Milestones**:
- **M9.1**: Comprehensive review (Week 47)
  - Technical accuracy review
  - Code testing across all chapters
  - Cross-reference validation
- **M9.2**: Supplementary materials completion (Week 48)
  - Complete glossary (all 25+ terms)
  - FAQ compilation
  - Research papers curation
  - Datasets documentation
- **M9.3**: Assessment system finalization (Week 49)
  - All 8 automated quizzes tested
  - Lab report rubrics finalized
  - Capstone rubric validated
  - Progress tracking implementation
- **M9.4**: Final polish and deployment (Week 50)
  - Copy editing
  - Diagram consistency check
  - Performance optimization (page load times)
  - Final deployment to GitHub Pages
- **Deliverable**: Complete, polished, deployed course

---

### Phase 10: Post-Launch Support (Ongoing)

**Milestones**:
- **M10.1**: User feedback collection and bug fixes (Weeks 51-54)
- **M10.2**: First update cycle (Quarter 1 post-launch)
  - Address user issues
  - Update deprecated dependencies
  - Add clarifications where needed
- **M10.3**: Annual major update (Year 1 post-launch)
  - Update ROS2 version if new LTS released
  - Refresh AI/ML frameworks
  - Add new research papers

---

### Timeline Summary

| Phase | Weeks | Duration | Major Deliverables |
|-------|-------|----------|-------------------|
| 0: Setup | 1-2 | 2 weeks | Infrastructure, templates, dev environment |
| 1: Module 1 | 3-6 | 4 weeks | Foundations (4 chapters) |
| 2: Module 2 | 7-11 | 5 weeks | Kinematics (5 chapters) |
| 3: Module 3 | 12-16 | 5 weeks | Dynamics & Control (5 chapters) |
| 4: Module 4 | 17-22 | 6 weeks | Perception (5 chapters) |
| 5: Module 5 | 23-28 | 6 weeks | Bipedal Locomotion (5 chapters) |
| 6: Module 6 | 29-36 | 8 weeks | AI & ML (5 chapters) |
| 7: Module 7 | 37-40 | 4 weeks | HRI (4 chapters) |
| 8: Module 8 | 41-46 | 6 weeks | Integration (3 chapters + 3 projects) |
| 9: Refinement | 47-50 | 4 weeks | Course-wide polish |
| 10: Post-Launch | 51+ | Ongoing | Support and updates |

**Total Development Time**: ~50 weeks (~12 months)

**Team Size**: 3-5 people (2-4 technical writers + 1-2 developers)

**Estimated Effort**:
- Technical writing: ~2,000-2,500 hours
- Code development: ~800-1,000 hours
- Review and testing: ~400-500 hours
- **Total**: ~3,200-4,000 hours

---

## 10. Cross-Module Knowledge Dependencies

This section maps the prerequisite relationships between modules to ensure proper knowledge sequencing and to help learners understand what prior knowledge is needed for each module.

### Dependency Graph

```
Module 1 (Foundations)
    ↓
    ├──→ Module 2 (Kinematics) ──→ Module 3 (Dynamics & Control)
    │         ↓                           ↓
    │         ├──────────────────────────┼──→ Module 5 (Locomotion) ──→ Module 6 (AI & ML)
    │         │                          │              ↓                       ↓
    │    Module 4 (Perception) ──────────┤              └───────────────────────┼──→ Module 8 (Integration)
    │         ↓                          │                                      ↑
    │         └──────────────────────────┴──→ Module 7 (HRI) ────────────────┘
    │
    └──────────────────────────────────────────────────────────────────────────┘
```

---

### Detailed Dependency Matrix

| Target Module | Required Prerequisites | Recommended Prerequisites | Specific Knowledge Required |
|---------------|----------------------|--------------------------|----------------------------|
| **Module 1: Foundations** | - Python programming<br>- C++ basics<br>- Linear algebra<br>- Calculus<br>- Linux CLI | - Git basics<br>- NumPy/SciPy | *Entry point* - External prerequisites only |
| **Module 2: Kinematics** | **Module 1**:<br>- Ch. 2: Transformation mathematics<br>- Ch. 4: ROS2 basics | **Module 1**:<br>- Ch. 3: Robot anatomy (DOF) | - Rotation matrices<br>- Homogeneous transforms<br>- ROS2 package creation |
| **Module 3: Dynamics & Control** | **Module 1**:<br>- Ch. 2: Math foundations<br>- Ch. 4: ROS2<br>**Module 2**:<br>- Ch. 5-6: FK/IK<br>- Ch. 7: Trajectories | **Module 2**:<br>- Ch. 9: Whole-body control | - Jacobians<br>- Numerical differentiation<br>- State-space representation |
| **Module 4: Perception** | **Module 1**:<br>- Ch. 2: Math (linear algebra)<br>- Ch. 4: ROS2 | **Module 2**:<br>- Ch. 5-6: Coordinate transforms | - Matrix operations<br>- ROS2 topics/services<br>- Python NumPy |
| **Module 5: Locomotion** | **Module 1**:<br>- Ch. 2: Math<br>**Module 2**:<br>- All chapters (FK/IK critical)<br>**Module 3**:<br>- Ch. 10-11: Dynamics, control theory | **Module 3**:<br>- Ch. 12-14: Advanced control | - Inverse kinematics<br>- PID control<br>- Dynamics computation<br>- Trajectory planning |
| **Module 6: AI & ML** | **Module 1**:<br>- Ch. 2: Math (calculus for gradients)<br>- Ch. 4: ROS2<br>**Module 2**:<br>- Ch. 5-6: FK/IK (for NN applications)<br>**Module 3**:<br>- Ch. 10: Dynamics (for model-based RL) | **Module 5**:<br>- Ch. 20-21: Locomotion (for RL examples) | - Gradient descent concepts<br>- Python programming (PyTorch)<br>- Dynamics models<br>- Simulation environments |
| **Module 7: HRI** | **Module 1**:<br>- Ch. 4: ROS2<br>**Module 4**:<br>- Ch. 15: Computer vision<br>- Ch. 16: Object detection | **Module 2**:<br>- Ch. 9: Whole-body control<br>**Module 3**:<br>- Ch. 13: Force control | - OpenCV basics<br>- ROS2 services/actions<br>- Camera calibration<br>- Pose estimation |
| **Module 8: Integration** | **All Modules 1-7**<br>(Varies by capstone project choice) | - | **Project 1 (Service Robot)**:<br>Modules 1, 2, 3, 4, 7<br><br>**Project 2 (Bipedal Walker)**:<br>Modules 2, 3, 5, 6<br><br>**Project 3 (Assembly Robot)**:<br>Modules 2, 3, 4, 7 |

---

### Chapter-Level Dependencies

**Critical Dependencies** (must complete before proceeding):

1. **Module 1, Chapter 2 → All Modules**
   - Transformation mathematics is foundational for all robotics
   - Rotation representations used throughout

2. **Module 1, Chapter 4 → All Modules**
   - ROS2 is the communication backbone for all practical work

3. **Module 2, Chapters 5-6 → Modules 3, 5, 8**
   - FK/IK required for control (Module 3), locomotion (Module 5), integration (Module 8)

4. **Module 3, Chapter 11 → Module 5**
   - Control theory (especially PID) required for locomotion controllers

5. **Module 4, Chapters 15-16 → Module 7**
   - Computer vision fundamentals required for HRI

6. **Module 6, Chapter 27 → Module 8, Capstone Project 2**
   - Deep RL required for Learning-Based Bipedal Walker

---

### Concept Dependencies Across Modules

| Concept | Introduced In | Used In | Critical For |
|---------|--------------|---------|--------------|
| **Homogeneous Transforms** | M1, Ch. 2 | M2 (all), M3, M4, M5 | FK/IK, sensor fusion, motion planning |
| **Jacobian Matrix** | M2, Ch. 6 | M3 (Ch. 11-12), M5 (Ch. 21-22) | Velocity control, whole-body control |
| **ROS2 Topics/Services** | M1, Ch. 4 | All modules | Communication between perception, planning, control |
| **PID Control** | M3, Ch. 11 | M5 (all), M6 (Ch. 29) | Locomotion, model-based control |
| **Kalman Filtering** | M4, Ch. 18 | M5 (Ch. 23), M7 (Ch. 33) | State estimation, sensor fusion, intent prediction |
| **Reinforcement Learning** | M6, Ch. 26-27 | M5 (Ch. 24), M8 (Capstone 2) | Learning locomotion, adaptive control |
| **Object Detection** | M4, Ch. 16 | M7 (Ch. 32-33), M8 (Capstone 1, 3) | HRI, manipulation tasks |

---

### Learning Path Flexibility

While the modules are designed for sequential completion, there is some flexibility for learners with specific interests:

**Alternative Path 1: Perception-Focused**
```
Module 1 → Module 4 → Module 7 → Module 2 → Module 8 (Capstone 1 or 3)
```
*Best for*: Computer vision engineers, machine perception specialists

**Alternative Path 2: Control-Focused**
```
Module 1 → Module 2 → Module 3 → Module 5 → Module 8 (Capstone 2)
```
*Best for*: Controls engineers, dynamics specialists

**Alternative Path 3: AI/ML-Focused**
```
Module 1 → Module 2 (Ch. 5-6 only) → Module 3 (Ch. 10-11 only) → Module 6 → Module 5 → Module 8 (Capstone 2)
```
*Best for*: Machine learning researchers applying to robotics

**Standard Path (Recommended)**:
```
Module 1 → Module 2 → Module 3 → Module 4 → Module 5 → Module 6 → Module 7 → Module 8
```
*Best for*: Comprehensive understanding, preparing for full-stack robotics roles

---

### Prerequisite Checking Mechanism

To support students in understanding dependencies, the course will include:

1. **Chapter-Level Prerequisites Section** (in each chapter):
   ```markdown
   ## Prerequisites

   **Required**:
   - Module 1, Chapter 2: Homogeneous Transformations
   - Module 1, Chapter 4: ROS2 Topics and Services

   **Recommended**:
   - Module 2, Chapter 5: Forward Kinematics

   **Self-Check**:
   - Can you compute a transformation matrix from Euler angles?
   - Can you create a ROS2 publisher and subscriber?
   ```

2. **Module Overview Page** (interactive dependency diagram using Mermaid per clarification Q5):
   ```mermaid
   graph TD
       M1[Module 1: Foundations] --> M2[Module 2: Kinematics]
       M1 --> M4[Module 4: Perception]
       M2 --> M3[Module 3: Dynamics]
       M2 --> M5[Module 5: Locomotion]
       M3 --> M5
       M4 --> M7[Module 7: HRI]
       M5 --> M6[Module 6: AI/ML]
       M6 --> M8[Module 8: Integration]
       M7 --> M8
   ```

3. **Automated Progress Tracker** (FR-014):
   - JavaScript component tracking chapter completion
   - Visual indicators showing which chapters are unlocked based on prerequisites
   - Warning system if student attempts to skip critical prerequisites

---

## Summary and Next Steps

This implementation plan provides a complete architecture for the Physical AI & Humanoid Robotics Course, covering all 10 requested areas:

✅ **1. Finalized module list**: 8 modules with clear focus areas
✅ **2. Chapters inside each module**: 36 chapters with detailed organization
✅ **3. Sub-sections for each chapter**: Comprehensive sub-section breakdown (full detail in Module 1, summary for others)
✅ **4. Practical labs and projects**: 36 practical sessions + 3 capstone projects with complete scaffolding
✅ **5. Tools, libraries, and hardware**: Comprehensive technology stack and optional hardware
✅ **6. Learning progression roadmap**: Week-by-week progression with skill progression matrix
✅ **7. Approximate page count**: 705-830 pages total (100,000-170,000 words)
✅ **8. Docusaurus folder structure**: Complete directory structure with sidebar configuration
✅ **9. Milestone timeline**: 50-week development plan with 10 phases
✅ **10. Cross-module dependencies**: Detailed dependency graph and prerequisite matrix

### Recommended Next Steps

1. **Review and approve this plan** - Ensure alignment with all stakeholders
2. **Run `/sp.tasks`** - Generate detailed, dependency-ordered task list for implementation
3. **Execute Phase 0 (Weeks 1-2)** - Set up infrastructure and templates
4. **Begin Phase 1 (Weeks 3-6)** - Start content creation with Module 1

### Plan Artifacts to be Created

Based on the plan template structure, the following additional artifacts will be generated:

1. **research.md** - Technology research and decisions (Phase 0)
2. **content-structure.md** - Complete sub-section breakdown for all 36 chapters
3. **docusaurus-config.md** - Detailed Docusaurus configuration guide
4. **milestone-timeline.md** - Gantt chart and detailed milestone tracking
5. **knowledge-dependencies.md** - Complete prerequisite matrix with self-check quizzes

These artifacts will be generated as part of the planning phase and will inform the `/sp.tasks` command.

---

**Plan Status**: ✅ **COMPLETE - READY FOR TASK GENERATION**

**Next Command**: `/sp.tasks` to decompose this plan into actionable, dependency-ordered tasks
