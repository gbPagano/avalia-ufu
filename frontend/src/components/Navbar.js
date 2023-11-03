import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav class="sticky top-0 flex justify-between items-stretch gap-2 p-1 text-white bg-slate-900 bg-opacity-50 backdrop-blur-xl w-full">
      <Link to="/" class="bg-darkblue text-white flex pl-3 pt-2 pb-0">
        <h1 class="text-4xl text-cyan-500 font-custom font-bold p-3 hover:text-cyan-200">
          WikiProf
        </h1>
      </Link>
      <ul class="font-custom flex list-none gap-10 pr-8">
        <li class="h-full flex items-center p-0.5">
          <Link class=" hover:text-cyan-500" to="/professores">
            Professores
          </Link>
        </li>
        <li class="h-full flex items-center p-0.5">
          <Link class=" hover:text-cyan-500" to="/disciplinas">
            Disciplinas
          </Link>
        </li>
        <li class="h-full flex items-center p-0.5">
          <Link class=" hover:text-cyan-500" to="/sobre">
            Sobre
          </Link>
        </li>
      </ul>
    </nav>
  );
}
