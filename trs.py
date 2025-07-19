import { motion } from "framer-motion";
import { useState } from "react";

export default function LineToInfinity() {
  const [stage, setStage] = useState(0);

  const stages = [
    {
      path: "M 50 100 H 450", // Line
      label: "Line",
    },
    {
      path: "M 250 100 m -150, 0 a 150,150 0 1,0 300,0 a 150,150 0 1,0 -300,0", // Circle
      label: "Circle",
    },
    {
      path: "M 150 100 C 100 0, 400 0, 350 100 C 400 200, 100 200, 150 100 Z", // Infinity symbol with smoother Bezier
      label: "Infinity",
    },
  ];

  const handleClick = () => {
    setStage((prev) => (prev + 1) % stages.length);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-white">
      <motion.svg
        width="500"
        height="200"
        viewBox="0 0 500 200"
        onClick={handleClick}
        className="cursor-pointer"
      >
        <motion.path
          d={stages[stage].path}
          fill="none"
          stroke="#000"
          strokeWidth="6"
          initial={{ pathLength: 0 }}
          animate={{ pathLength: 1 }}
          transition={{ duration: 1.2, ease: "easeInOut" }}
        />
      </motion.svg>
      <p className="text-xl mt-4">{stages[stage].label}</p>
      <p className="text-sm text-gray-500">Click shape to transform</p>
    </div>
  );
}
