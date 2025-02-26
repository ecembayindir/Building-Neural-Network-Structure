package com.sorbonne;

import org.neo4j.graphdb.*;
import org.neo4j.logging.Log;
import org.neo4j.procedure.*;

import java.util.Map;
import java.util.stream.Stream;

public class CreateNeuron {
    @Context
    public Log log;

    @Context
    public GraphDatabaseService db;

    @Procedure(name = "nn.createNeuron", mode = Mode.WRITE)
    @Description("Creates a neuron with specified properties")
    public Stream<CreateResult> createNeuron(
            @Name("id") String id,
            @Name("layer") String layer,
            @Name("type") String type,
            @Name("activation_function") String activation_function
    ) {
        try (Transaction tx = db.beginTx()) {
            tx.execute(
                    "CREATE (n:Neuron {" +
                            "id: $id, " +
                            "layer: $layer, " +
                            "type: $type, " +
                            "bias: 0.0, " +
                            "output: null, " +
                            "m_bias: 0.0, " +
                            "v_bias: 0.0, " +
                            "activation_function: $activation_function" +
                            "})",
                    Map.of(
                            "id", id,
                            "layer", layer,
                            "type", type,
                            "activation_function", activation_function
                    )
            );

            tx.commit();
            return Stream.of(new CreateResult("ok"));
        } catch (Exception e) {
            log.error("Error creating neuron: " + e.getMessage(), e);
            return Stream.of(new CreateResult("ko"));
        }
    }

    @Procedure(name = "nn.createRelationShipsNeuron", mode = Mode.WRITE)
    @Description("Creates a relationship between two neurons")
    public Stream<CreateResult> createRelationShipsNeuron(
            @Name("from_id") String from_id,
            @Name("to_id") String to_id,
            @Name("weight") Double weight
    ) {
        try (Transaction tx = db.beginTx()) {
            tx.execute(
                    "MATCH (n1:Neuron {id: $from_id}) " +
                            "MATCH (n2:Neuron {id: $to_id}) " +
                            "CREATE (n1)-[:CONNECTED_TO {weight: $weight}]->(n2)",
                    Map.of(
                            "from_id", from_id,
                            "to_id", to_id,
                            "weight", weight
                    )
            );

            tx.commit();
            return Stream.of(new CreateResult("ok"));
        } catch (Exception e) {
            log.error("Error creating relationship: " + e.getMessage(), e);
            return Stream.of(new CreateResult("ko"));
        }
    }

    public static class CreateResult {
        public final String result;

        public CreateResult(String result) {
            this.result = result;
        }
    }
}