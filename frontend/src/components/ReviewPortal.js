import { useState } from "react";
import { createPortal } from "react-dom";
import ReviewModalContent from "./ReviewModalContent.js";

export default function ReviewPortal({ nomeDisc, reviews }) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button
        class="px-5 py-3 text-sm text-gray-100 rounded-full bg-cyan-600 hover:bg-cyan-900"
        onClick={() => setShowModal(true)}
      >
        Ver reviews
      </button>
      {showModal &&
        createPortal(
          <ReviewModalContent
            nomeDisc={nomeDisc}
            reviews={reviews}
            onClose={() => setShowModal(false)}
          />,
          document.body
        )}
    </>
  );
}
