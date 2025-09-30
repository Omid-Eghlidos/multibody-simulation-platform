/**
 * @file SimulateForm.tsx
 * @description Simulation form component for submitting initial conditions of two bodies.
 */

import React, { useCallback, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Form, FormField, FormLabel } from '@radix-ui/react-form';
import { Button, Card, Flex, Heading, Separator, TextField } from '@radix-ui/themes';
import _ from 'lodash';
import { Routes } from '@/routes'; 
import type { FormData, FormValue } from '@/interfaces/features/simulation/SimulateForm.interface';
import { container, card } from '@/styles/features/simulation/SimulateForm.styles';

/**
 * SimulateForm component.
 * Renders input fields for two bodies and submits simulation request to backend.
 */
const SimulateForm: React.FC = () => {
    const navigate = useNavigate();

    /**
     * React state: holds all input values for Body1 and Body2.
     */
    const [formData, setFormData] = useState<FormData>({
        Body1: { position: { x: -0.73, y: 0, z: 0 }, velocity: { x: 0, y: -0.0015, z: 0 }, mass: 1 },
        Body2: { position: { x: 60.34, y: 0, z: 0 }, velocity: { x: 0, y: 0.13, z: 0 }, mass: 0.0123 },
    });

    /**
     * Handles input field changes.
     *
     * @param e - React input change event
     *
     * Uses lodash `set` to update nested fields inside formData.
     * Converts blank string to '' and non-empty to number.
     */
    const handleChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        const newValue: FormValue = value === '' ? '' : parseFloat(value);
        setFormData((prev) => _.set({ ...prev }, name, newValue));
    }, []);

    /**
     * Handles form submission.
     *
     * @param e - Form submit event
     *
     * Sends POST request to backend API with formData.
     * Navigates to simulation results route if successful.
     */
    const handleSubmit = useCallback(
        async (e: React.FormEvent) => {
            e.preventDefault();
            try {
                const response = await fetch('http://localhost:8000/api/v1/simulation/run', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData),
                });
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                navigate(Routes.SIMULATION);
            } catch (error) {
                console.error('Error submitting simulation:', error);
            }
        },
        [formData, navigate]
    );

    return (
        <div style={container}>
            <Card style={card}>
                <Heading as="h2" size="4" weight="bold" mb="4">
                    Run a Simulation
                </Heading>
                <Link to={Routes.SIMULATION}>View previous simulation</Link>
                <Separator size="4" my="5" />
                <Form onSubmit={handleSubmit}>
                    {/* ==================== Body1 Input Section ==================== */}
                    <Heading as="h3" size="3" weight="bold">Body1</Heading>

                    {/* Position inputs (x, y, z) */}
                    {['x', 'y', 'z'].map((axis) => (
                        <FormField key={`Body1.position.${axis}`} name={`Body1.position.${axis}`}>
                            <FormLabel htmlFor={`Body1.position.${axis}`}>
                                Initial {axis.toUpperCase()}-position
                            </FormLabel>
                            <TextField.Root
                                type="number"
                                id={`Body1.position.${axis}`}
                                name={`Body1.position.${axis}`}
                                value={formData.Body1.position[axis as 'x' | 'y' | 'z']}
                                onChange={handleChange}
                                required
                            />
                        </FormField>
                    ))}

                    {/* Velocity inputs (x, y, z) */}
                    {['x', 'y', 'z'].map((axis) => (
                        <FormField key={`Body1.velocity.${axis}`} name={`Body1.velocity.${axis}`}>
                            <FormLabel htmlFor={`Body1.velocity.${axis}`}>
                                Initial {axis.toUpperCase()}-velocity
                            </FormLabel>
                            <TextField.Root
                                type="number"
                                id={`Body1.velocity.${axis}`}
                                name={`Body1.velocity.${axis}`}
                                value={formData.Body1.velocity[axis as 'x' | 'y' | 'z']}
                                onChange={handleChange}
                                required
                            />
                        </FormField>
                    ))}

                    {/* Mass */}
                    <FormField name="Body1.mass">
                        <FormLabel htmlFor="Body1.mass">Mass</FormLabel>
                        <TextField.Root
                            type="number"
                            id="Body1.mass"
                            name="Body1.mass"
                            value={formData.Body1.mass}
                            onChange={handleChange}
                            required
                        />
                    </FormField>

                    {/* ==================== Body2 Input Section ==================== */}
                    <Heading as="h3" size="3" weight="bold" mt="4">Body2</Heading>

                    {/* Position inputs (x, y, z) */}
                    {['x', 'y', 'z'].map((axis) => (
                        <FormField key={`Body2.position.${axis}`} name={`Body2.position.${axis}`}>
                            <FormLabel htmlFor={`Body2.position.${axis}`}>
                                Initial {axis.toUpperCase()}-position
                            </FormLabel>
                            <TextField.Root
                                type="number"
                                id={`Body2.position.${axis}`}
                                name={`Body2.position.${axis}`}
                                value={formData.Body2.position[axis as 'x' | 'y' | 'z']}
                                onChange={handleChange}
                                required
                            />
                        </FormField>
                    ))}

                    {/* Velocity inputs (x, y, z) */}
                    {['x', 'y', 'z'].map((axis) => (
                        <FormField key={`Body2.velocity.${axis}`} name={`Body2.velocity.${axis}`}>
                            <FormLabel htmlFor={`Body2.velocity.${axis}`}>
                                Initial {axis.toUpperCase()}-velocity
                            </FormLabel>
                            <TextField.Root
                                type="number"
                                id={`Body2.velocity.${axis}`}
                                name={`Body2.velocity.${axis}`}
                                value={formData.Body2.velocity[axis as 'x' | 'y' | 'z']}
                                onChange={handleChange}
                                required
                            />
                        </FormField>
                    ))}

                    {/* Mass */}
                    <FormField name="Body2.mass">
                        <FormLabel htmlFor="Body2.mass">Mass</FormLabel>
                        <TextField.Root
                            type="number"
                            id="Body2.mass"
                            name="Body2.mass"
                            value={formData.Body2.mass}
                            onChange={handleChange}
                            required
                        />
                    </FormField>

                    {/* Submit button */}
                    <Flex justify="center" m="5">
                        <Button type="submit">Submit</Button>
                    </Flex>
                </Form>
            </Card>
        </div>
    );
};

export default SimulateForm;
