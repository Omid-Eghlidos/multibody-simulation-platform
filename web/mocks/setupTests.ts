/**
 * setupTests.ts
 * -----------------
 * Global mocks and setup for Vitest.
 */
import "@testing-library/jest-dom"; 
import { vi } from "vitest";
import SimulationPageMock from "./SimulationPageMock";

// Mock Plotly-based SimulationPage with a lightweight stub
vi.mock("../src/features/simulation/SimulationPage", () => ({
    default: SimulationPageMock,
}));
