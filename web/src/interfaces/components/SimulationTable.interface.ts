/**
 * @file SimulationTable.interface.ts
 * @description Props definition for SimulationTable component.
 */

import type { DataFrame } from '@/interfaces/features/simulation/SimulationPage.interface';

/**
 * Props for SimulationTable.
 */
export interface SimulationTableProps {
    /** Initial state of agents from simulation (positions + velocities). */
    initialState: DataFrame;
}
