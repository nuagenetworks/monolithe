import {{ class_prefix }}Attribute from 'service/{{ class_prefix }}Attribute';
import {{ superclass_name }} from 'service/{{ superclass_name }}';
import {{ class_prefix }}Exception from 'service/{{ class_prefix }}Exception';

/* Represents an abstract named entity, with attributes name and description
*/

export default class {{ class_prefix }}AbstractNamedEntity extends {{ superclass_name }} {
    constructor(...args) {
        super(...args);
        this.defineProperties({
            name: undefined,
            description: undefined,
        });
    }

    static attributeDescriptors = {
        ...{{ superclass_name }}.attributeDescriptors,
        name: new {{ class_prefix }}Attribute({
            localName: 'name',
            attributeType: {{ class_prefix }}Attribute.ATTR_TYPE_STRING,
            isRequired: true,
            canOrder: true,
            canSearch: true,
            minLength: 1,
            maxLength: 255
        }),
        description: new {{ class_prefix }}Attribute({
            localName: 'description',
            attributeType: {{ class_prefix }}Attribute.ATTR_TYPE_STRING,
            canSearch: true,
            minLength: 0,
            maxLength: 255
        }),
    }

    get RESTName() {
        throw new {{ class_prefix }}Exception('Not implemented');
    }
}

