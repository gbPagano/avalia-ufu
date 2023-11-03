import ReviewSentOKModalContent from "./ReviewSentOKModalContent";
import { useState } from "react";
import { createPortal } from "react-dom";

export default function ReviewSentOKPortal() {
  const [showModal, setShowModal] = useState(false);

  return (
    showModal &&
    createPortal(
      <ReviewSentOKModalContent onClose={() => setShowModal(true)} />,
      document.body
    )
  );
}
