import axios from "axios";

export default {
    GET_ES_INFO: ({ commit }, { search, sort }) => {
        console.log("SORT", sort);
        const data = !!search
            ? {
                  query: {
                      multi_match: {
                          query: search,
                          fields: [
                              "customers_id",
                              "customers_firstname",
                              "customers_lastname",
                              "customers_email_address",
                          ],
                      },
                  },
              }
            : {};
        return axios(
            `/csv_info/_search?size=50&pretty${!!sort ? `&sort=${sort}` : ""}`,
            {
                baseURL: "http://localhost:9200",
                method: "POST",
                data,
            }
        ).then((res) => {
            console.log(res.data);
            commit("SET_CSV_INFO", res.data.hits.hits);
        });
    },
};
