import {
    useState
} from "react";

import {
    FaArrowUp
} from "react-icons/fa";



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
max-w-3xl
mx-auto
relative
"
        >


            <input

                value={question}

                onChange={
                    e => setQuestion(e.target.value)
                }


                onKeyDown={
                    e => {

                        if (e.key === "Enter")
                            send();

                    }

                }



                placeholder="
Message RAG Assistant...
"


                className="
w-full
bg-[#2f2f2f]
rounded-3xl
px-5
py-4
pr-14
outline-none
text-white
placeholder-gray-500
border
border-white/10
focus:border-white/20
"

            />





            <button

                onClick={send}

                className="
absolute
right-3
top-3

w-9
h-9

rounded-full

bg-white
text-black

flex
items-center
justify-center

hover:bg-gray-200

"

            >


                <FaArrowUp />

            </button>




        </div>


    )

}