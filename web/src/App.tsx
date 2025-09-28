/**
 * @file App.tsx
 * @description Root component: sets up Radix theme and router.
 */

import { Theme } from '@radix-ui/themes';
import '@radix-ui/themes/styles.css';
import React from 'react';
import { createBrowserRouter, RouterProvider, Navigate } from 'react-router-dom';
import { Routes } from '@/routes';
import SimulationPage from '@/features/simulation/SimulationPage';
import SimulateForm from '@/features/simulation/SimulateForm';
import NotFoundPage from '@/pages/NotFoundPage';

/**
 * App component.
 * Provides Radix Theme and routing for the application.
 */
const App: React.FC = () => {
    const router = createBrowserRouter([
        {
            path: '/',
            element: <Navigate to={Routes.FORM} replace />
        },
        {
            path: Routes.FORM,
            element: <SimulateForm />,
            errorElement: <NotFoundPage />,
        },
        {
            path: Routes.SIMULATION,
            element: <SimulationPage />,
        },
        {
            path: Routes.NOT_FOUND,
            element: <NotFoundPage />,
        },
    ]);

    return (
        <Theme appearance="dark" accentColor="iris" grayColor="mauve" radius="small">
            <RouterProvider router={router} />
        </Theme>
    );
};

export default App;
