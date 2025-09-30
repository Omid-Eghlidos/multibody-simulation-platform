/**
 * App.test.tsx
 * -----------------
 * Simple proof-of-concept test for the React frontend.
 * Ensures that the App renders the simulation form.
 */

import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import App from "../src/App";

describe("App", () => {
    it("renders the simulation form", () => {
        render(<App />);
        expect(screen.getByText(/Submit/i)).toBeInTheDocument();
    });
});

