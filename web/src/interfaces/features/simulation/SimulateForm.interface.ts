/**
 * @file SimulateForm.interface.ts
 * @description Type definitions and props for SimulateForm component.
 */

/**
 * Represents a form field value.
 * Empty string is used for blank input, otherwise a number.
 */
export type FormValue = number | '';

/**
 * Shape of body data for the simulation form.
 */
export interface BodyData {
    position: {
        x: FormValue;
        y: FormValue;
        z: FormValue;
    };
    velocity: {
        x: FormValue;
        y: FormValue;
        z: FormValue;
    };
    mass: FormValue;
}

/**
 * Full form state structure for two-body simulation input.
 */
export interface FormData {
    Body1: BodyData;
    Body2: BodyData;
}

/**
 * Props for the SimulateForm component.
 */
export interface SimulateFormProps {}
