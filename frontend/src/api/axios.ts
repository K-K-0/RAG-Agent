import axios from "axios";

export default axios.create({
    baseURL:"https://backend-522310987799.asia-south1.run.app",
    headers:{
        "Content-Type":"application/json"
    }
});