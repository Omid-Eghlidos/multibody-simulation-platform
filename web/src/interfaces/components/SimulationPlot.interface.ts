/**
 * @file SimulationPlot.interface.ts
 * @description Props definition for SimulationPlot component.
 */

import type { PlottedAgentData } from '@/interfaces/features/simulation/SimulationPage.interface';

/**
 * Props for SimulationPlot.
 */
export interface SimulationPlotProps {
    /** Title of the plot (e.g., "Position" or "Velocity"). */
    title: string;

    /** Array of plotted agent data formatted for Plotly. */
    data: PlottedAgentData[];
}
