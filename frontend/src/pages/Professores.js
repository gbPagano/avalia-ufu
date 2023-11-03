import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import usericon from "./img/user.png";
import CreateReviewPortal from "../components/CreateReviewPortal";
import ReviewSentOKModalContent from "../components/ReviewSentOKModalContent";

import Api from "../api/Api.js";

export default function Professores() {
  const [profs, setProfs] = useState([]);
  const [faculs, setFaculs] = useState([]);
  const [showReviewSentOKModal, setShowReviewSentOKModal] = useState(false);

  useEffect(() => {
    Api.getProfs().then((profs) => setProfs(profs));
    Api.getFaculs().then((faculs) => setFaculs(faculs));
  }, []);

  function handleSortChange(e) {
    Api.getProfs(e.target.value).then((profs) => setProfs(profs));
  }

  function handleFaculChange(e) {}

  const handleReviewSent = (showReviewSentOKModalBool) => {
    setShowReviewSentOKModal(showReviewSentOKModalBool);
  };

  return (
    <>
      <ReviewSentOKModalContent
        isOpen={showReviewSentOKModal}
        onClose={() => setShowReviewSentOKModal(false)}
      />
      <div class="pt-6 pb-4 flex flex-row gap-10 w-1/3 items-center">
        <div class="flex items-center">
          <p class="text-white font-custom inline pr-4 pl-12">Ordenar por: </p>
          <select onChange={handleSortChange} class="inline p-2 rounded-xl">
            <option value="">nenhum filtro</option>
            <option value="a-z">nome crescente</option>
            <option value="z-a">nome decrescente</option>
            <option value="Nn">maior nota</option>
            <option value="nN">menor nota</option>
          </select>
        </div>
        <div class="flex flex-row w-48 items-center justify-between">
          <p class="font-custom  text-white">Faculdade:</p>
          <select onChange={handleFaculChange} class="inline p-2 rounded-xl">
            <option value="-1">Todas</option>
            {faculs.map((facul) => {
              return <option value={facul.id}>{facul.nome}</option>;
            })}
          </select>
        </div>
      </div>
      <div class="grid p-4 gap-y-0 gap-x-6 grid-cols-5">
        {profs.map((prof) => {
          return (
            <div
              id="prof-card-container"
              class="flex flex-wrap flex-grow-0 content-between gap-5 font-custom py-7 px-7 max-w-sm h-5/6 max-h-fit bg-gray-700 rounded-2xl shadow-lg shadow-black"
            >
              <img
                class="block self-start justify-self-center mx-auto h-14 rounded-full"
                src={usericon}
                alt="Ícone do professor"
              />
              <div
                id="prof-card-content"
                class="text-center space-y-2 sm:text-left h-2/3 w-full"
              >
                <div class="flex justify-between">
                  <h2 class="text-xl text-cyan-500 font-semibold">
                    {prof.nome}
                  </h2>
                  <p class="text-black">{prof.faculdade.nome}</p>
                </div>
                <p class="inline text-white">Nota média: </p>
                <p class="inline text-green-400 text-lg font-bold">
                  {prof.nota.toFixed(1)}
                </p>
                <p class="text-white">Disciplinas lecionadas:</p>
                <div id="discs-list" class="overflow-y-scroll h-2/3">
                  <ul>
                    {prof.disciplinas_lecionadas.map((disciplina) => (
                      <>
                        <li class="p-0.5">
                          <button class="px-4 py-1 text-sm text-white rounded-full border border-gray-500 hover:border-gray-950">
                            <Link to={"/disciplina/" + disciplina.id}>
                              {disciplina.nome}
                            </Link>
                          </button>
                        </li>
                      </>
                    ))}
                  </ul>
                </div>
              </div>
              <div class="flex flex-grow-0 w-full h-1/6 justify-end bg-opacity-25">
                <div class="self-end mb-4">
                  <CreateReviewPortal
                    prof={prof}
                    discs={prof.disciplinas_lecionadas}
                    handleReviewSent={handleReviewSent}
                  />
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </>
  );
}
