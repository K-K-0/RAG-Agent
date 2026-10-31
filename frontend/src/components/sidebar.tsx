import {
    FaPlus,
    FaHistory,
    FaDatabase,
    FaCog,
    FaFilePdf,
    FaTrash,
    FaRobot
} from "react-icons/fa";



interface Props {

    clearChat:()=>void;

}



export default function Sidebar({
    clearChat
}:Props){


return (

<div

className="
w-72
h-screen

bg-[#171717]

border-r
border-white/10

flex
flex-col

text-white

"

>



{/* Logo */}

<div

className="
p-5
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

AI Document Search

</p>


</div>


</div>


</div>









{/* New Chat */}

<div
className="
p-4
"
>


<button

className="
w-full

flex
items-center
gap-3

px-4
py-3

rounded-xl

bg-white/5

border
border-white/10

hover:bg-white/10

transition

"

>


<FaPlus/>

New Chat


</button>


</div>









{/* Navigation */}

<div

className="
px-4
space-y-2
"

>



<button

className="
w-full

flex
items-center
gap-3

px-4
py-3

rounded-lg

text-gray-300

hover:bg-white/10

transition

"

>

<FaHistory/>

History

</button>







<button

className="
w-full

flex
items-center
gap-3

px-4
py-3

rounded-lg

text-gray-300

hover:bg-white/10

transition

"

>

<FaFilePdf/>

Documents

</button>







<button

className="
w-full

flex
items-center
gap-3

px-4
py-3

rounded-lg

text-gray-300

hover:bg-white/10

transition

"

>

<FaDatabase/>

Knowledge Base

</button>








<button

className="
w-full

flex
items-center
gap-3

px-4
py-3

rounded-lg

text-gray-300

hover:bg-white/10

transition

"

>

<FaCog/>

Settings

</button>



</div>









{/* Document Status */}

<div

className="
mx-4
mt-6
p-4

rounded-xl

bg-white/5

border
border-white/10

"

>


<p
className="
text-xs
text-gray-400
mb-2
"
>

Knowledge Base

</p>



<div
className="
flex
items-center
gap-2
text-sm
"
>


<span
className="
w-2
h-2
rounded-full
bg-green-400
"
/>


PDF Indexed


</div>


<p
className="
text-xs
text-gray-500
mt-2
"
>

Hybrid Search Active

</p>


</div>









{/* Bottom */}

<div

className="
mt-auto
p-4

"

>


<button

onClick={clearChat}

className="
w-full

flex
items-center
gap-3

px-4
py-3

rounded-xl

text-red-400

hover:bg-red-500/10

transition

"

>

<FaTrash/>

Clear Chat


</button>


</div>







</div>


)


}