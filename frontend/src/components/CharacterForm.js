// frontend/src/components/CharacterForm.js
import React, { useState } from 'react';
import axios from 'axios';

function CharacterForm() {
    const [name, setName] = useState("");
    const [classType, setClassType] = useState("");
    const [attributes, setAttributes] = useState({ strength: 0, dexterity: 0 });
    const [message, setMessage] = useState("");
    const [error, setError] = useState("");
    const [createdCharacter, setCreatedCharacter] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!name || !classType) {
            setError("Name and Class Type are required.");
            return;
        }
        if (attributes.strength < 0 || attributes.dexterity < 0) {
            setError("Attributes cannot be negative.");
            return;
        }
        setError("");

        try {
            const response = await axios.post("http://localhost:8000/api/v1/character/create", {
                name,
                class_type: classType,
                attributes
            });
            setMessage(`Character created successfully! ID: ${response.data.character_id}`);
            setCreatedCharacter(response.data.character_data); // Store character data for display
            setName("");
            setClassType("");
            setAttributes({ strength: 0, dexterity: 0 });
        } catch (error) {
            setError("Error creating character. Please try again.");
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Name:
                    <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
                </label>
                <label>Class Type:
                    <input type="text" value={classType} onChange={(e) => setClassType(e.target.value)} required />
                </label>
                <label>Strength:
                    <input
                        type="number"
                        value={attributes.strength}
                        onChange={(e) => setAttributes({ ...attributes, strength: parseInt(e.target.value) })}
                        min="0"
                        required
                    />
                </label>
                <label>Dexterity:
                    <input
                        type="number"
                        value={attributes.dexterity}
                        onChange={(e) => setAttributes({ ...attributes, dexterity: parseInt(e.target.value) })}
                        min="0"
                        required
                    />
                </label>
                <button type="submit">Create Character</button>

                {error && <p style={{ color: 'red' }}>{error}</p>}
                {message && <p style={{ color: 'green' }}>{message}</p>}
            </form>

            {createdCharacter && (
                <div>
                    <h2>Character Details:</h2>
                    <p><strong>Name:</strong> {createdCharacter.name}</p>
                    <p><strong>Class Type:</strong> {createdCharacter.class_type}</p>
                    <p><strong>Strength:</strong> {createdCharacter.attributes.strength}</p>
                    <p><strong>Dexterity:</strong> {createdCharacter.attributes.dexterity}</p>
                </div>
            )}
        </div>
    );
}

export default CharacterForm;
