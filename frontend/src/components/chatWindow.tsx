import { useState, useRef, useEffect } from "react";
import { askQuestion } from "../api/rag";
import ChatInput from "./chatInput";
import ChatMessage from "./chatMessage";


interface Message {

    role: "user" | "assistant";

    content: string;

}


export default function ChatWindow() {


    const [messages, setMessages] = useState<Message[]>([]);

    const [loading, setLoading] = useState(false);


    const bottomRef = useRef<HTMLDivElement>(null);



    useEffect(()=>{

        bottomRef.current?.scrollIntoView({
            behavior:"smooth"
        });

    },[messages,loading]);





    const sendMessage = async(question:string)=>{


        setMessages(prev=>[
            ...prev,
            {
                role:"user",
                content:question
            }
        ]);



        setLoading(true);



        try{

            const response = await askQuestion(question);


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
                    content:"Something went wrong."
                }
            ]);

        }


        setLoading(false);

    };





    return (

        <div
        className="
        h-screen
        bg-[#212121]
        text-white
        flex
        flex-col
        "
        >



            {/* Header */}

            <div
            className="
            h-14
            border-b
            border-white/10
            flex
            items-center
            justify-center
            "
            >

                <h1 className="
                font-semibold
                text-lg
                ">
                    RAG Assistant
                </h1>


            </div>






            {/* Messages */}


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
                    h-[60vh]
                    flex
                    items-center
                    justify-center
                    text-center
                    "
                    >

                        <div>

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
                            Ask questions from your documents
                        </p>

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
                    "
                    >

                        Thinking...

                    </div>

                }




                <div ref={bottomRef}/>


                </div>


            </div>





            {/* Input */}

            <ChatInput
            onSend={sendMessage}
            />


        </div>

    );

}