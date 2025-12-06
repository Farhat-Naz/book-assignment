import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * Sidebar configuration for Physical AI & Humanoid Robotics Course
 *
 * Structure: 8 Modules → 36 Chapters → Labs & Assessments
 * Per Clarification Q2: Hierarchical sidebar with modules as top-level categories
 */
const sidebars: SidebarsConfig = {
  courseSidebar: [
    {
      type: 'doc',
      id: 'index',
      label: 'Course Overview',
    },
    {
      type: 'doc',
      id: 'prerequisites/index',
      label: 'Prerequisites',
    },

    // Module 1: Foundations of Physical AI
    {
      type: 'category',
      label: 'Module 1: Foundations',
      collapsed: false,
      link: {
        type: 'doc',
        id: 'module-01-foundations/index',
      },
      items: [
        'module-01-foundations/ch01-intro-physical-ai',
        'module-01-foundations/ch02-math-foundations',
        'module-01-foundations/ch03-robot-anatomy',
        'module-01-foundations/ch04-ros2-architecture',
        {
          type: 'category',
          label: 'Labs',
          items: [
            'labs/lab-01-environment-setup/index',
            'labs/lab-02-transformation-math/index',
            'labs/lab-03-urdf-models/index',
            'labs/lab-04-multi-node-system/index',
          ],
        },
      ],
    },

    // Module 2: Robot Kinematics
    {
      type: 'category',
      label: 'Module 2: Kinematics',
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
        {
          type: 'category',
          label: 'Labs',
          items: [
            'labs/lab-05-forward-kinematics/index',
            'labs/lab-06-inverse-kinematics/index',
            'labs/lab-07-trajectory-generation/index',
            'labs/lab-08-motion-planning/index',
            'labs/lab-09-whole-body-motion/index',
          ],
        },
      ],
    },

    // Module 3: Dynamics and Control
    {
      type: 'category',
      label: 'Module 3: Dynamics & Control',
      collapsed: true,
      link: {
        type: 'doc',
        id: 'module-03-dynamics-control/index',
      },
      items: [
        'module-03-dynamics-control/ch10-rigid-body-dynamics',
        'module-03-dynamics-control/ch11-control-theory',
        'module-03-dynamics-control/ch12-advanced-control',
        'module-03-dynamics-control/ch13-force-control',
        'module-03-dynamics-control/ch14-real-time-control',
        {
          type: 'category',
          label: 'Labs',
          items: [
            'labs/lab-10-dynamics-simulation/index',
            'labs/lab-11-pid-control/index',
            'labs/lab-12-advanced-control/index',
            'labs/lab-13-force-control/index',
            'labs/lab-14-real-time-systems/index',
          ],
        },
      ],
    },

    // Module 4: Perception
    {
      type: 'category',
      label: 'Module 4: Perception',
      collapsed: true,
      link: {
        type: 'doc',
        id: 'module-04-perception/index',
      },
      items: [
        'module-04-perception/ch15-computer-vision',
        'module-04-perception/ch16-object-detection',
        'module-04-perception/ch17-slam',
        'module-04-perception/ch18-sensor-fusion',
        'module-04-perception/ch19-point-clouds',
        {
          type: 'category',
          label: 'Labs',
          items: [
            'labs/lab-15-computer-vision/index',
            'labs/lab-16-object-detection/index',
            'labs/lab-17-slam/index',
            'labs/lab-18-sensor-fusion/index',
            'labs/lab-19-point-clouds/index',
          ],
        },
      ],
    },

    // Module 5: Bipedal Locomotion
    {
      type: 'category',
      label: 'Module 5: Locomotion',
      collapsed: true,
      link: {
        type: 'doc',
        id: 'module-05-locomotion/index',
      },
      items: [
        'module-05-locomotion/ch20-bipedal-fundamentals',
        'module-05-locomotion/ch21-walking-controllers',
        'module-05-locomotion/ch22-balance-control',
        'module-05-locomotion/ch23-terrain-locomotion',
        'module-05-locomotion/ch24-running-jumping',
        {
          type: 'category',
          label: 'Labs',
          items: [
            'labs/lab-20-bipedal-fundamentals/index',
            'labs/lab-21-walking-simulation/index',
            'labs/lab-22-balance-recovery/index',
            'labs/lab-23-terrain-adaptation/index',
            'labs/lab-24-dynamic-locomotion/index',
          ],
        },
      ],
    },

    // Module 6: AI and Machine Learning
    {
      type: 'category',
      label: 'Module 6: AI & Learning',
      collapsed: true,
      link: {
        type: 'doc',
        id: 'module-06-ai-learning/index',
      },
      items: [
        'module-06-ai-learning/ch25-ml-fundamentals',
        'module-06-ai-learning/ch26-reinforcement-learning',
        'module-06-ai-learning/ch27-deep-rl',
        'module-06-ai-learning/ch28-imitation-learning',
        'module-06-ai-learning/ch29-model-based-rl',
        {
          type: 'category',
          label: 'Labs',
          items: [
            'labs/lab-25-ml-basics/index',
            'labs/lab-26-rl-fundamentals/index',
            'labs/lab-27-deep-rl-training/index',
            'labs/lab-28-imitation-learning/index',
            'labs/lab-29-model-based-rl/index',
          ],
        },
      ],
    },

    // Module 7: Human-Robot Interaction
    {
      type: 'category',
      label: 'Module 7: HRI',
      collapsed: true,
      link: {
        type: 'doc',
        id: 'module-07-hri/index',
      },
      items: [
        'module-07-hri/ch30-hri-fundamentals',
        'module-07-hri/ch31-speech-nlp',
        'module-07-hri/ch32-gesture-recognition',
        'module-07-hri/ch33-collaborative-tasks',
        {
          type: 'category',
          label: 'Labs',
          items: [
            'labs/lab-30-speech-recognition/index',
            'labs/lab-31-nlp-integration/index',
            'labs/lab-32-gesture-control/index',
            'labs/lab-33-human-collaboration/index',
          ],
        },
      ],
    },

    // Module 8: Integration and Capstone
    {
      type: 'category',
      label: 'Module 8: Integration',
      collapsed: true,
      link: {
        type: 'doc',
        id: 'module-08-integration/index',
      },
      items: [
        'module-08-integration/ch34-system-architecture',
        'module-08-integration/ch35-testing-validation',
        'module-08-integration/ch36-ethics-future',
        {
          type: 'category',
          label: 'Capstone Projects',
          items: [
            'module-08-integration/capstone-project-1',
            'module-08-integration/capstone-project-2',
            'module-08-integration/capstone-project-3',
          ],
        },
        {
          type: 'category',
          label: 'Labs',
          items: [
            'labs/lab-34-system-integration/index',
            'labs/lab-35-testing-validation/index',
            'labs/lab-36-ethics-case-studies/index',
          ],
        },
      ],
    },

    // Supplementary Resources
    {
      type: 'category',
      label: 'Resources',
      collapsed: true,
      items: [
        'resources/datasets',
        'resources/tools-setup',
        'resources/hardware-guide',
        'resources/troubleshooting',
        'resources/research-papers',
        'resources/external-resources',
      ],
    },

    // Assessments
    {
      type: 'category',
      label: 'Assessments',
      collapsed: true,
      items: [
        {
          type: 'category',
          label: 'Module Quizzes',
          items: [
            'assessments/quizzes/module-01-quiz',
            'assessments/quizzes/module-02-quiz',
            'assessments/quizzes/module-03-quiz',
            'assessments/quizzes/module-04-quiz',
            'assessments/quizzes/module-05-quiz',
            'assessments/quizzes/module-06-quiz',
            'assessments/quizzes/module-07-quiz',
            'assessments/quizzes/module-08-quiz',
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

export default sidebars;
