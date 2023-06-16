import axios from "axios";
import { useState, useEffect } from "react";

function useFetch(url) {
    const [content, setContent] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios
            .get(url)
            .then((response) => {
                setContent(response);
            })
            .catch((err) => {
                setError(err);
                console.log(err);
            })
            .finally(() => {
                setLoading(false);
            });
    }, [url]);
    console.log(content);

    return { content, error, loading };
}

export default useFetch;
