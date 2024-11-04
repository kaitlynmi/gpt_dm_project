import React from 'react';
import './App.css';
import PlayerActions from './components/PlayerView/PlayerActions';
import CharacterForm from './components/CharacterForm';

function App() {
    return (
        <div className="App">
            <h1>GPT-Powered Dungeon Master</h1>
            <PlayerActions />
            <CharacterForm />
        </div>
    );
}

export default App;
