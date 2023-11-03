import "./App.css";
import Navbar from "./components/Navbar";

import About from "./pages/About";
import Disciplinas from "./pages/Disciplinas";
import Disciplina from "./components/Disciplina";
import Professores from "./pages/Professores";
import Home from "./pages/Home";

import { Route, Routes } from "react-router-dom";

function App() {
  return (
    <div class="bg-gradient-to-br from-slate-950 to-slate-500">
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/professores" element={<Professores />} />
        <Route path="/disciplina/:id" element={<Disciplina />} />
        <Route path="/disciplinas" element={<Disciplinas />} />
        <Route path="/sobre" element={<About />} />
      </Routes>
    </div>
  );
}

export default App;
