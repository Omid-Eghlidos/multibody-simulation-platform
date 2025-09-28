/**
 * @file SimulationPage.interface.ts
 * @description Type definitions for SimulationPage component and simulation data.
 */

// Input data from the backend
export type AgentData = {
    position: { x: number; y: number; z: number };
    velocity: { x: number; y: number; z: number };
};

export type DataFrame = Record<string, AgentData>;
export type DataPoint = [number, number, DataFrame];

// Transformed data for Plotly
export interface PlottedAgentData {
    x: number[];
    y: number[];
    z: number[];
    type: 'scatter3d';
    mode: 'lines+markers';
    marker: { size: number };
    line: { width: number };
}

export type PlottedFrame = Record<string, PlottedAgentData>;
