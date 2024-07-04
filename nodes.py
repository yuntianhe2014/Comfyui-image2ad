from .utils import save_images,get_ads


class Image2ads:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.
    IS_CHANGED:
        optional method to control when the node is re executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "image": ("IMAGE", ),
                "int_field": ("INT", {
                    "default": 15, 
                    "min": 15, #Minimum value
                    "max": 50, #Maximum value
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
            },
        }

    RETURN_TYPES = ("SEQUENCE",)
    RETURN_NAMES = ("sequence",)
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "Image2ads"
    

    def test(self, image,int_field):
        fp = save_images(image)
        result = get_ads(fp,int_field)
        # response=send_get_request(image)
        # q = get_des(response)
        # result = get_ads(q,int_field)
        try:
            result = json.loads("["+result.split("[")[-1].split("]")[0]+"]")
        except:
            result = result.split("\n")
        return (result,)


class Image2ads_Literal:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "sequence": ("SEQUENCE", )
            },
        }

    RETURN_TYPES = ("SEQUENCE", )
    RETURN_NAMES = ("sequence", )
    FUNCTION = "go"
    CATEGORY = "Image2ads"

    def go(self, sequence):
        return ([sequence], )   
                

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "Image2ads": Image2ads,
    "Image2ads_Literal":Image2ads_Literal
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Image2ads": "image to ads",
    "Image2ads_Literal":"Literal"
}
