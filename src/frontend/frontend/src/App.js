import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';

import About from './pages/About';
import Disciplinas from './pages/Disciplinas';
import Disciplina from './components/Disciplina';
import Professores from './pages/Professores';
import Home from './pages/Home'

import { Route, Routes } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/professores" element={<Professores />} />
        <Route path="/disciplinas" element={<Disciplinas />} />
        <Route path="/disciplina/:id" element={<Disciplina />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  );
}

export default App;
