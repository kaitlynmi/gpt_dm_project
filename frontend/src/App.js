import React from 'react';
import './App.css';
import PlayerActions from './components/PlayerView/PlayerActions';

function App() {
    return (
        <div className="App">
            <h1>GPT-Powered Dungeon Master</h1>
            <PlayerActions />
        </div>
    );
}

export default App;
