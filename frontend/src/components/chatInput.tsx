import { useState } from "react";
import { FaArrowUp } from "react-icons/fa";


interface Props {

    onSend: (question: string) => void;

}



export default function ChatInput({
    onSend
}: Props) {


    const [question, setQuestion]
        =
        useState("");



    const send = () => {


        if (!question.trim())
            return;


        onSend(question);

        setQuestion("");

    };



    return (

        <div
            className="
border-t
border-white/10
bg-[#212121]
p-4
"
        >


            <div
                className="
max-w-3xl
mx-auto
relative
"
            >


                <input

                    className="
w-full

bg-[#2f2f2f]

rounded-3xl

px-5
py-4

pr-14

outline-none

text-white

placeholder-gray-400

"

                    placeholder="
Message RAG Assistant...
"

                    value={question}

                    onChange={
                        e => setQuestion(e.target.value)
                    }


                    onKeyDown={
                        e => {
                            if (e.key === "Enter")
                                send()
                        }
                    }

                />



                <button

                    onClick={send}

                    className="
absolute
right-3
top-3

bg-white
text-black

w-9
h-9

rounded-full

flex
items-center
justify-center

"

                >


                    <FaArrowUp />

                </button>


            </div>


        </div>

    );

}