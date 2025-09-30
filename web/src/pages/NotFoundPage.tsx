/**
 * @file NotFoundPage.tsx
 * @description Displays a 404 page when no matching route is found.
 */

import React from 'react';
import { Heading, Flex } from '@radix-ui/themes';
import type { NotFoundPageProps } from '@/interfaces/pages/NotFoundPage.interface';
import { container } from '@/styles/pages/NotFoundPage.styles';

/**
 * NotFoundPage component.
 */
const NotFoundPage: React.FC<NotFoundPageProps> = () => {
    return (
        <Flex justify="center" align="center" style={container}>
            <Heading as="h1" size="8" weight="bold">
                404 - Page Not Found
            </Heading>
        </Flex>
    );
};

export default NotFoundPage;
