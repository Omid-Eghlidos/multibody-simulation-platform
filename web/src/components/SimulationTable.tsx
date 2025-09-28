/**
 * @file SimulationTable.tsx
 * @description Renders initial position and velocity of agents in a Radix Table.
 */

import React from 'react';
import { Table } from '@radix-ui/themes';
import type { SimulationTableProps } from '@/interfaces/components/SimulationTable.interface';
import { tableRoot } from '@/styles/components/SimulationTable.styles';

/**
 * SimulationTable component.
 * Displays initial positions and velocities of agents in tabular form.
 */
const SimulationTable: React.FC<SimulationTableProps> = ({ initialState }) => {
    return (
        <Table.Root style={tableRoot}>
            <Table.Header>
                <Table.Row>
                    <Table.ColumnHeaderCell>Agent</Table.ColumnHeaderCell>
                    <Table.ColumnHeaderCell>Initial Position (x,y,z)</Table.ColumnHeaderCell>
                    <Table.ColumnHeaderCell>Initial Velocity (x,y,z)</Table.ColumnHeaderCell>
                </Table.Row>
            </Table.Header>
            <Table.Body>
                {Object.entries(initialState).map(([agentId, { position, velocity }]) =>
                    position ? (
                        <Table.Row key={agentId}>
                            <Table.RowHeaderCell>{agentId}</Table.RowHeaderCell>
                            <Table.Cell>
                                ({position.x}, {position.y}, {position.z})
                            </Table.Cell>
                            <Table.Cell>
                                ({velocity.x}, {velocity.y}, {velocity.z})
                            </Table.Cell>
                        </Table.Row>
                    ) : null
                )}
            </Table.Body>
        </Table.Root>
    );
};

export default SimulationTable;
