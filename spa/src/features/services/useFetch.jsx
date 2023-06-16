import axios from "axios";
import { useState, useEffect } from "react";

axios.defaults.baseURL = "http://localhost:5000/api";

function useFetch(axiosParams) {
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    async function fetchData(axiosParams) {
        try {
            const result = await axios.request(axiosParams);
            setResponse(result.data);
        } catch (error) {
            setError(error);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        fetchData(axiosParams);
    }, [axiosParams]);

    return { response, loading, error };
}

export default useFetch;
