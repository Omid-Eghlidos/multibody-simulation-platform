/**
 * @file SimulationPlot.tsx
 * @description Renders a 3D scatter plot (position or velocity) using Plotly.
 */

import React from 'react';
import Plot from 'react-plotly.js';
import type { SimulationPlotProps } from '../interfaces/components/SimulationPlot.interface';
import { plotContainer } from '@/styles/components/SimulationPlot.styles';

/**
 * SimulationPlot component.
 * Displays a 3D scatter plot of simulation data.
 */
const SimulationPlot: React.FC<SimulationPlotProps> = ({ title, data }) => {
    return (
        <Plot
            style={plotContainer}
            data={data}
            layout={{
                title: { text: title },
                scene: {
                    xaxis: { title: { text: 'X' } },
                    yaxis: { title: { text: 'Y' } },
                    zaxis: { title: { text: 'Z' } },
                },
                autosize: true,
                dragmode: 'turntable',
            }}
            useResizeHandler
            config={{ scrollZoom: true }}
        />
    );
};

export default SimulationPlot;
