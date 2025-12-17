/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import React, {type ReactNode, useEffect} from 'react';
import {HtmlClassNameProvider} from '@docusaurus/theme-common';
import {DocProvider} from '@docusaurus/plugin-content-docs/client';
import DocItemMetadata from '@theme/DocItem/Metadata';
import DocItemLayout from '@theme/DocItem/Layout';
import type {Props} from '@theme/DocItem';

export default function DocItem(props: Props): ReactNode {
  const docHtmlClassName = `docs-doc-id-${props.content.metadata.id}`;
  const MDXComponent = props.content;

  useEffect(() => {
    // This script is for the ChatKit chatbot integration.
    // It needs to be configured with a valid ChatKit ID.
    // The chatbot should be configured to use the `window.chatKitSelectedText`
    // variable to get the selected text on the page.

    const handleMouseUp = () => {
      const selection = window.getSelection()?.toString();
      if (selection) {
        (window as any).chatKitSelectedText = selection;
        console.log('Selected text for chatbot:', selection);
      } else {
        delete (window as any).chatKitSelectedText;
      }
    };

    document.addEventListener('mouseup', handleMouseUp);

    const chatKitScript = document.createElement('script');
    chatKitScript.src = 'https://cdn.chatkit.com/sdk.js';
    chatKitScript.async = true;
    // IMPORTANT: Replace "YOUR_CHATKIT_ID" with your actual ChatKit ID
    chatKitScript.setAttribute('data-chatkit-id', 'YOUR_CHATKIT_ID'); 
    document.body.appendChild(chatKitScript);

    return () => {
      document.removeEventListener('mouseup', handleMouseUp);
      if (document.body.contains(chatKitScript)) {
        document.body.removeChild(chatKitScript);
      }
    };
  }, []);


  return (
    <DocProvider content={props.content}>
      <HtmlClassNameProvider className={docHtmlClassName}>
        <DocItemMetadata />
        {/* Placeholder for per-chapter content personalization button */}
        {/* Placeholder for per-chapter Urdu translation button */}
        <DocItemLayout>
          <MDXComponent />
        </DocItemLayout>
      </HtmlClassNameProvider>
    </DocProvider>
  );
}
