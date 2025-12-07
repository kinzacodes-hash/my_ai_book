import React from 'react';

import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function Home() {
  return (
    <Layout title="Humanoid Robotics Book" description="Physical AI & Humanoid Robotics Course">
      <header className="hero hero--primary" style={{ background: 'linear-gradient(to right, #0f172a, #1e293b)', color: '#fff', padding: '6rem 0' }}>
        <div className="container text--center">
          <h1 style={{ fontSize: '3.5rem', marginBottom: '1rem' }}>Building the Future: Physical AI & Humanoid Robotics</h1>
          <p style={{ fontSize: '1.5rem', marginBottom: '2rem' }}>A comprehensive guide to embodied intelligence, Sim2Real transfer, and autonomous agents.</p>
          <Link className="button button--lg button--secondary" to="/docs/introduction/intro" style={{ background: '#06b6d4', border: 'none' }}>
            Start Learning
          </Link>
        </div>
      </header>

      <main className="container margin-vert--lg">
        <section className="row">
          <div className="col col--4">
            <h2>Interactive Learning</h2>
            <p>Embedded RAG Chatbot for real-time Q&A on book content.</p>
          </div>
          <div className="col col--4">
            <h2>Sim2Real Focus</h2>
            <p>From simulation in Isaac Sim to real humanoid deployment.</p>
          </div>
          <div className="col col--4">
            <h2>Agentic Workflow</h2>
            <p>Powered by Claude Code Subagents and reusable Skills.</p>
          </div>
        </section>

        <section>
          <h2>Module Preview</h2>
          <div className="row">
            {[
              { label: 'Module 00 – Introduction', to: '/docs/introduction/intro' },
              { label: 'Module 01 – Foundations', to: '/docs/foundations/foundations' },
              { label: 'Module 02 – ROS 2', to: '/docs/ros2/ros2' },
              { label: 'Module 03 – Simulation', to: '/docs/simulation/simulation' },
              { label: 'Module 04 – NVIDIA Isaac', to: '/docs/isaac/isaac' },
              { label: 'Module 05 – Kinematics', to: '/docs/kinematics/kinematics' },
              { label: 'Module 06 – VLA Models', to: '/docs/vla/vla' },
              { label: 'Module 07 – Capstone', to: '/docs/capstone/capstone' },
            ].map((m, idx) => (
              <div key={idx} className="col col--3 margin-bottom--md">
                <Link to={m.to} className="card padding--md text--center" style={{ background: '#1e293b', color: '#06b6d4' }}>
                  {m.label}
                </Link>
              </div>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}
