/**
 * @file SimulationPage.tsx
 * @description Main page displaying latest simulation results (plots + table).
 */

import React, { useEffect, useState } from 'react';
import { Flex, Heading, Separator } from '@radix-ui/themes';
import { Link } from 'react-router-dom';
import { Routes } from '@/routes';
import { fetchLatestSimulation } from '@/api/simulation';
import type { DataFrame, DataPoint, PlottedFrame, PlottedAgentData } from '@/interfaces/features/simulation/SimulationPage.interface';
import SimulationPlot from '@/components/SimulationPlot';
import SimulationTable from '@/components/SimulationTable';
import { rootContainer } from '@/styles/features/simulation/SimulationPage.styles';

/**
 * SimulationPage component.
 * Fetches simulation data on mount and renders position + velocity plots and initial state table.
 */
const SimulationPage: React.FC = () => {
    const [positionData, setPositionData] = useState<PlottedAgentData[]>([]);
    const [velocityData, setVelocityData] = useState<PlottedAgentData[]>([]);
    const [initialState, setInitialState] = useState<DataFrame>({});

    useEffect(() => {
        let canceled = false;

        /**
         * Converts backend DataPoint[] into PlottedAgentData[] for Plotly.
         *
         * @param data - Array of DataPoint
         */
        const transformData = (data: DataPoint[]) => {
            const updatedPositionData: PlottedFrame = {};
            const updatedVelocityData: PlottedFrame = {};

            setInitialState(data[0][2]);

            const baseData = () => ({
                x: [] as number[],
                y: [] as number[],
                z: [] as number[],
                type: 'scatter3d' as const,
                mode: 'lines+markers' as const,
                marker: { size: 4 },
                line: { width: 2 },
            });

            data.forEach(([_, __, frame]) => {
                for (let [agentId, val] of Object.entries(frame)) {
                    if (agentId === 'time' || agentId === 'timeStep') continue;
                    const { position, velocity } = val;

                    updatedPositionData[agentId] = updatedPositionData[agentId] || baseData();
                    updatedPositionData[agentId].x.push(position.x);
                    updatedPositionData[agentId].y.push(position.y);
                    updatedPositionData[agentId].z.push(position.z);

                    updatedVelocityData[agentId] = updatedVelocityData[agentId] || baseData();
                    updatedVelocityData[agentId].x.push(velocity.x);
                    updatedVelocityData[agentId].y.push(velocity.y);
                    updatedVelocityData[agentId].z.push(velocity.z);
                }
            });

            setPositionData(Object.values(updatedPositionData));
            setVelocityData(Object.values(updatedVelocityData));
        };

        fetchLatestSimulation()
            .then((data) => {
                if (!canceled) transformData(data);
            })
            .catch((err) => console.error('Error fetching simulation:', err));

        return () => {
            canceled = true;
        };
    }, []);

    return (
        <div style={rootContainer}>
            <Flex direction="column" m="4" width="100%" justify="center" align="center">
                <Heading as="h1" size="8" weight="bold" mb="4">
                    Simulation Data
                </Heading>
                <Link to={Routes.FORM}>Define new simulation parameters</Link>
                <Separator size="4" my="5" />

                {/* Plots */}
                <Flex direction="row" width="100%" justify="center">
                    <SimulationPlot title="Position" data={positionData} />
                    <SimulationPlot title="Velocity" data={velocityData} />
                </Flex>

                {/* Initial state table */}
                <Flex justify="center" width="100%" m="4">
                    <SimulationTable initialState={initialState} />
                </Flex>
            </Flex>
        </div>
    );
};

export default SimulationPage;
