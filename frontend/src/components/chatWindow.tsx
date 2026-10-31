import {
    useState,
    useRef,
    useEffect
} from "react";


import {
    FaRobot,
    FaFilePdf,
    FaTrash,
    FaBolt
} from "react-icons/fa";


import Sidebar from "./sidebar";

import ChatMessage from "./chatMessage";

import ChatInput from "./chatInput";


import { askQuestion } from "../api/rag";



interface Message {

    role: "user" | "assistant";

    content: string;

}



export default function ChatWindow(){



    const [messages,setMessages]
    =
    useState<Message[]>([]);



    const [loading,setLoading]
    =
    useState(false);



    const bottomRef =
    useRef<HTMLDivElement>(null);





    useEffect(()=>{


        bottomRef.current?.scrollIntoView({
            behavior:"smooth"
        });


    },[messages,loading]);







    const clearChat = ()=>{

        setMessages([]);

    };







    const sendMessage = async(question:string)=>{


        if(!question.trim())
            return;



        setMessages(prev=>[

            ...prev,

            {
                role:"user",
                content:question
            }

        ]);



        setLoading(true);



        try{


            const response =
            await askQuestion(question);



            setMessages(prev=>[

                ...prev,

                {
                    role:"assistant",
                    content:response.answer
                }

            ]);



        }

        catch{


            setMessages(prev=>[

                ...prev,

                {

                    role:"assistant",

                    content:"⚠️ Something went wrong."

                }

            ]);


        }



        setLoading(false);


    };









    return (


        <div

        className="
        h-screen
        flex
        bg-[#212121]
        text-white
        "

        >




            {/* SIDEBAR */}

            <Sidebar

                clearChat={clearChat}

            />








            {/* MAIN AREA */}


            <div

            className="
            flex-1
            flex
            flex-col
            "

            >






                {/* HEADER */}


                <div

                className="
                h-16
                flex
                items-center
                justify-between

                px-6

                border-b
                border-white/10

                "

                >



                    <div

                    className="
                    flex
                    items-center
                    gap-3
                    "

                    >



                        <div

                        className="
                        w-9
                        h-9
                        rounded-lg

                        bg-green-500/20

                        flex
                        items-center
                        justify-center
                        "

                        >

                            <FaRobot
                            className="
                            text-green-400
                            "
                            />


                        </div>





                        <div>


                            <h1
                            className="
                            font-semibold
                            "
                            >

                                RAG Assistant

                            </h1>



                            <p
                            className="
                            text-xs
                            text-gray-400
                            "
                            >

                                AI powered document search

                            </p>



                        </div>




                    </div>






                    <button

                    onClick={clearChat}

                    className="
                    flex
                    items-center
                    gap-2

                    px-3
                    py-2

                    rounded-lg

                    bg-white/5

                    border
                    border-white/10

                    text-sm

                    hover:bg-white/10

                    "

                    >

                        <FaTrash/>

                        Clear


                    </button>




                </div>









                {/* CHAT CONTENT */}



                <div

                className="
                flex-1
                overflow-y-auto
                "

                >



                    <div

                    className="
                    max-w-3xl
                    mx-auto

                    px-4
                    py-8

                    space-y-8

                    "

                    >






                    {

                    messages.length===0 &&


                    <div

                    className="
                    h-[65vh]

                    flex
                    flex-col

                    items-center
                    justify-center

                    text-center

                    "

                    >



                        <div

                        className="
                        w-20
                        h-20

                        rounded-full

                        bg-green-500/10

                        flex
                        items-center
                        justify-center

                        mb-5

                        "

                        >

                            <FaRobot

                            className="
                            text-4xl
                            text-green-400
                            "

                            />


                        </div>





                        <h2

                        className="
                        text-3xl
                        font-semibold
                        "

                        >

                            How can I help you?

                        </h2>




                        <p

                        className="
                        text-gray-400
                        mt-3
                        "

                        >

                            Ask questions from your PDF documents

                        </p>







                        <div

                        className="
                        flex
                        flex-wrap
                        justify-center
                        gap-3

                        mt-8

                        "

                        >



                        {


                        [

                            "Explain BSc completion timeline",

                            "What is refund policy?",

                            "Tell me about minors",

                            "Explain Computer System Design"

                        ]


                        .map(item=>(



                            <button


                            key={item}


                            onClick={()=>sendMessage(item)}



                            className="

                            px-4
                            py-3

                            rounded-xl

                            bg-[#2f2f2f]

                            border
                            border-white/10

                            text-sm

                            text-gray-300

                            hover:bg-[#3a3a3a]

                            "

                            >


                                {item}


                            </button>



                        ))



                        }



                        </div>




                    </div>



                    }









                    {


                    messages.map((msg,index)=>(


                        <ChatMessage

                        key={index}

                        role={msg.role}

                        content={msg.content}

                        />


                    ))


                    }









                    {

                    loading &&


                    <div

                    className="
                    text-gray-400
                    animate-pulse
                    "

                    >

                        🤖 Thinking...


                    </div>


                    }





                    <div ref={bottomRef}/>



                    </div>



                </div>









                {/* INPUT AREA */}


                <div

                className="
                border-t
                border-white/10

                py-3

                "

                >



                    <div

                    className="
                    max-w-3xl
                    mx-auto

                    flex
                    gap-2

                    text-xs
                    text-gray-500

                    mb-2

                    "

                    >


                        <FaBolt/>


                        RAG Mode • Hybrid Search • PDF Knowledge Base


                    </div>






                    <ChatInput

                    onSend={sendMessage}

                    />




                </div>







            </div>





        </div>


    );


}