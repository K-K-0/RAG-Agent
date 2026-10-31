import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { FaUser, FaRobot } from "react-icons/fa";


interface Props {

role:"user"|"assistant";

content:string;

}



export default function ChatMessage({
role,
content
}:Props){


const user = role==="user";



return (

<div
className={`
flex
gap-4

${user
?"justify-end"
:"justify-start"
}

`}
>


{
!user &&

<div
className="
mt-1
text-green-400
"
>

<FaRobot/>

</div>

}



<div
className={`
max-w-3xl

text-[16px]

leading-7

${user
?
"bg-[#2f2f2f] rounded-3xl px-5 py-3"
:
""
}

`}
>


<ReactMarkdown

remarkPlugins={[remarkGfm]}

>

{content}

</ReactMarkdown>


</div>





{
user &&

<div
className="
mt-1
text-gray-400
"
>

<FaUser/>

</div>

}


</div>


);

}