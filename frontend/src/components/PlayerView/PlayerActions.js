import React, { useState } from 'react';
import axios from 'axios';

function PlayerActions() {
    const [result, setResult] = useState(null);
    const [diceSides, setDiceSides] = useState(20);

    const rollDice = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/v1/game/roll_dice?sides=${diceSides}`);
            setResult(response.data.result);
        } catch (error) {
            console.error("Error rolling the dice:", error);
        }
    };

    return (
        <div>
            <h2>Roll a Dice</h2>
            <input
                type="number"
                value={diceSides}
                onChange={(e) => setDiceSides(e.target.value)}
                placeholder="Enter number of sides"
            />
            <button onClick={rollDice}>Roll {diceSides}-sided Dice</button>
            {result && <p>Dice Result: {result}</p>}
        </div>
    );
}

export default PlayerActions;
