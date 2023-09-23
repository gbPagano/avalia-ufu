import { IoCheckmarkCircleSharp } from "react-icons/io5";
import chroma from "chroma-js";
import { createPortal } from "react-dom";

export default function ReviewSentOKModalContent({ isOpen, onClose }) {
  if (!isOpen) return null;
  return createPortal(
    <div
      id="review-sent-ok-modal"
      class="py-5 px-5 flex flex-col justify-between gap-2 rounded-lg text-white font-custom backdrop-blur-xl bg-opacity-70 shadow-lg shadow-gray-950 z-50 fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 bg-gray-950"
    >
      <IoCheckmarkCircleSharp
        size={40}
        color={chroma("white")}
        class="w-full"
      />
      <h2 class="w-full">Review enviada com sucesso!</h2>
      <div class="w-full flex justify-center">
        <button
          class="px-5 py-2 text-sm text-black font-bold rounded-full bg-cyan-100 hover:bg-cyan-200"
          onClick={onClose}
        >
          Fechar
        </button>
      </div>
    </div>,
    document.body
  );
}
