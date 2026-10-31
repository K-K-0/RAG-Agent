import API from "./axios";

export const askQuestion = async(question:string)=>{

    const response = await API.post("/chat",{
        question
    });

    return response.data;
}