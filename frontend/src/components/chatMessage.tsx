import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import {
    FaRobot,
    FaUser
} from "react-icons/fa";



interface Props {

    role: "user" | "assistant";

    content: string;

}



export default function ChatMessage({
    role,
    content
}: Props) {


    const user =
        role === "user";



    return (

        <div
            className={`
flex
gap-4

${user
                    ?
                    "justify-end"
                    :
                    "justify-start"
                }

`}
        >



            {
                !user &&

                <div
                    className="
text-green-400
mt-2
"
                >

                    <FaRobot />

                </div>

            }






            <div
                className={`
max-w-3xl
leading-7


${user
                        ?
                        "bg-[#2f2f2f] px-5 py-3 rounded-3xl"
                        :
                        "text-gray-200"
                    }

`}
            >


                <ReactMarkdown

                    remarkPlugins={[
                        remarkGfm
                    ]}

                    components={{

                        strong: ({ children }) => (

                            <strong
                                className="
text-green-400
"
                            >
                                {children}
                            </strong>

                        ),


                        h2: ({ children }) => (

                            <h2
                                className="
text-xl
font-bold
mt-5
mb-3
"
                            >
                                {children}
                            </h2>

                        ),


                        li: ({ children }) => (

                            <li
                                className="
ml-5
list-disc
"
                            >
                                {children}
                            </li>

                        )

                    }}

                >

                    {content}

                </ReactMarkdown>



            </div>






            {
                user &&

                <div
                    className="
text-gray-400
mt-2
"
                >

                    <FaUser />

                </div>

            }



        </div>


    )

}