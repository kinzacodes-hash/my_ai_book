/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The docs sidebar can be rendered either as a Category (group of doc cards) or as a Collapsible Category (group of links).
 */

const sidebars = {
  bookSidebar: [
    {
      type: 'category',
      label: 'Module 00 – Introduction',
      link: {type: 'doc', id: 'introduction/intro'},
      items: [
        'introduction/intro',
      ],
    },
    {
      type: 'category',
      label: 'Module 01 – Foundations',
      link: {type: 'doc', id: 'foundations/foundations'},
      items: [
        'foundations/foundations',
      ],
    },
    {
      type: 'category',
      label: 'Module 02 – ROS 2',
      link: {type: 'doc', id: 'ros2/ros2'},
      items: [
        'ros2/ros2',
      ],
    },
    {
      type: 'category',
      label: 'Module 03 – Simulation',
      link: {type: 'doc', id: 'simulation/simulation'},
      items: [
        'simulation/simulation',
      ],
    },
    {
      type: 'category',
      label: 'Module 04 – NVIDIA Isaac',
      link: {type: 'doc', id: 'isaac/isaac'},
      items: [
        'isaac/isaac',
      ],
    },
    {
      type: 'category',
      label: 'Module 05 – Kinematics',
      link: {type: 'doc', id: 'kinematics/kinematics'},
      items: [
        'kinematics/kinematics',
      ],
    },
    {
      type: 'category',
      label: 'Module 06 – VLA Models',
      link: {type: 'doc', id: 'vla/vla'},
      items: [
        'vla/vla',
      ],
    },
    {
      type: 'category',
      label: 'Module 07 – Capstone',
      link: {type: 'doc', id: 'capstone/capstone'},
      items: [
        'capstone/capstone',
      ],
    },
    {
      type: 'category',
      label: 'Appendices',
      items: [
        'appendices/cloud_vs_on_premise',
        'appendices/deploying_models_to_jetson',
        'appendices/hardware',
        'appendices/resources',
        'appendices/ros2_cheatsheet',
        'appendices/troubleshooting_isaac_sim',
      ],
    },
  ],
};

export default sidebars;