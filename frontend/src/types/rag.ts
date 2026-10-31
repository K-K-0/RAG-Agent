export interface Source{

    content:string;

    metadata:{
        page:number;
        source:string;
    }

}

export interface ChatResponse{

    question:string;

    answer:string;

    retrieved_chunks:Source[];

}