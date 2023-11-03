import { useState } from "react";
import { createPortal } from "react-dom";
import CreateReviewModalContent from "./CreateReviewModalContent";

export default function CreateReviewPortal({ prof, discs, handleReviewSent }) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button
        class="px-5 py-3 text-sm text-white rounded-full bg-cyan-600 hover:bg-cyan-900"
        onClick={() => setShowModal(true)}
      >
        Avaliar
      </button>
      {showModal &&
        createPortal(
          <CreateReviewModalContent
            discs={discs}
            prof={prof}
            onClose={() => setShowModal(false)}
            handleReviewSent={handleReviewSent}
          />,
          document.body
        )}
    </>
  );
}
