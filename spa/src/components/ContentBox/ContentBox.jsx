import { Layout, Spin, Alert, Col, Row } from "antd";
import RecipeCard from "../RecipeCard/RecipeCard";
import useFetch from "../../features/services/useFetch";

const { Content } = Layout;

function ContentBox(props) {
    const { response, loading, error } = useFetch("/recipes");
    return (
        <Content className="bg-white block">
            {loading ? (
                <Spin />
            ) : error ? (
                <Alert
                    message={error.request.status}
                    description={error.message}
                />
            ) : (
                <div className="p-6 bg-white">
                    <Row>
                        {response.results.map((recipe) => (
                            <Col
                                xs={{ span: 24 }}
                                sm={{ span: 12 }}
                                md={{ span: 8 }}
                                lg={{ span: 6 }}
                                gutter={10}
                                key={recipe.url}
                            >
                                <RecipeCard
                                    title={recipe.title}
                                    description={recipe.description}
                                />
                            </Col>
                        ))}
                    </Row>
                </div>
            )}
        </Content>
    );
}

export default ContentBox;
