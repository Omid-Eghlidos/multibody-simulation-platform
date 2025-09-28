/**
 * @file simulation.ts
 * @description API functions for simulation backend.
 */

import type { DataPoint } from '@/interfaces/features/simulation/SimulationPage.interface';

/**
 * Fetches the latest simulation results from backend.
 *
 * @returns Promise resolving to array of DataPoint
 * @throws Error if network request fails
 */
export async function fetchLatestSimulation(): Promise<DataPoint[]> {
    const response = await fetch('http://localhost:8000/api/v1/simulation/latest');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
}
