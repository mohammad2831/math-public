def clean_profile_picture(self):
        profile_picture = self.files.get('profile_picture')
        if profile_picture:
            import base64
            from io import BytesIO
            from PIL import Image

            image = Image.open(profile_picture)
            buffered = BytesIO()
            image.save(buffered, format=image.format)
            img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
            return img_base64
        return None