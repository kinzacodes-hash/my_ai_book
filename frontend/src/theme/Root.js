import React, { useEffect } from 'react';

export default function Root({ children }) {
  useEffect(() => {
    const chatBubbleUrl = "https://www.chatkit.app/embed/chat-bubble?api=http://127.0.0.1:8000/chat&title=Ask%20about%20Humanoid%20Robotics&position=bottom-right&theme=dark";

    const iframe = document.createElement("iframe");
    iframe.title = "Chatbot";
    iframe.src = chatBubbleUrl;
    iframe.width = "400px";
    iframe.height = "600px";
    iframe.style.position = "fixed";
    iframe.style.bottom = "20px";
    iframe.style.right = "20px";
    iframe.style.zIndex = "9999";
    iframe.style.border = "none";
    iframe.style.borderRadius = "10px";
    iframe.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.2)";

    document.body.appendChild(iframe);

    return () => {
      document.body.removeChild(iframe);
    };
  }, []);

  return <>{children}</>;
}