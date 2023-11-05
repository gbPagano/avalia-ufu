import { useState, useEffect } from "react";
import ReviewPortal from "../components/ReviewPortal.js";
import { BiTachometer } from "react-icons/bi";
import chroma from "chroma-js";

import Api from "../api/Api.js";

export default function Disciplinas() {
  const [data, setData] = useState([]);

  useEffect(() => {
    Api.getDiscs().then((discs) => setData(discs));
  }, []);

  function handleSortChange(e) {
    Api.getDiscs(e.target.value).then((discs) => setData(discs));
  }

  return (
    <>
      <div class="pt-6 pb-4">
        <p class="text-white font-custom inline pr-4 pl-12">Ordenar por: </p>
        <select onChange={handleSortChange} class="inline p-2 rounded-xl">
          <option value="">nenhum filtro</option>
          <option value="a-z">nome crescente</option>
          <option value="z-a">nome decrescente</option>
          <option value="hard">mais difícil</option>
          <option value="easy">menos difícil</option>
        </select>
      </div>
      <div
        id="disciplinas-container"
        class="grid p-4 gap-5 grid-cols-5 grid-rows-3"
      >
        {data.map((disciplina) => {
          return (
            <div
              id="disc-card-container"
              class="flex flex-wrap flex-grow-0 content-between gap-1 font-custom text-white py-7 px-7 max-w-sm h-6/7 bg-gray-700 rounded-2xl shadow-lg shadow-black"
            >
              <h2 class="text-xl font-bold w-full text-cyan-500">
                {disciplina.nome}
              </h2>
              <div class="w-full flex justify-between">
                <h3 class="text-md text-cyan-200">
                  {disciplina.faculdade.nome}
                </h3>
                <div class="w-1/6 flex justify-between items-center">
                  <BiTachometer
                    class="inline"
                    size={30}
                    color={chroma("gray").darken(0.5)}
                  />
                  <p class="inline text-green-400 text-lg font-bold">
                    {disciplina.dificuldade}
                  </p>
                </div>
              </div>
              <p class="w-full">Professores lecionando: </p>
              <ul class="pl-6 h-1/3 w-full overflow-y-scroll">
                {disciplina.professores_desta.map((prof) => (
                  <>
                    <li>
                      <button class="px-4 py-1 text-sm text-white rounded-full border border-gray-500">
                        {prof.nome}
                      </button>
                    </li>
                  </>
                ))}
              </ul>
              <div class="flex flex-grow-0 w-full h-1/6 justify-end bg-opacity-25">
                <ReviewPortal
                  nomeDisc={disciplina.nome}
                  reviews={disciplina.reviews_desta}
                />
              </div>
            </div>
          );
        })}
      </div>
    </>
  );
}
